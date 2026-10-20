// Figma token-compliance audit: read-only, current page only.
// Paste this code into a Figma JavaScript execution context with access to figma.
// It returns review candidates; it does not modify the file or certify token semantics.

// Optional: supply exact canonical master IDs for mixed-purpose pages (e.g. File Uploader).
// Empty means inventory every non-archived root component on the loaded page.
const CANONICAL_MASTER_IDS = [];

const page = figma.currentPage;
const collections = await figma.variables.getLocalVariableCollectionsAsync();
const variables = await figma.variables.getLocalVariablesAsync();
const collectionById = new Map(collections.map(c => [c.id, c.name]));
const variableById = new Map(variables.map(v => [v.id, v]));
const spacingValues = new Set(
  variables.filter(v => collectionById.get(v.variableCollectionId) === "Spacing")
    .map(v => Number(Object.values(v.valuesByMode)[0]))
    .filter(Number.isFinite)
);
const masters = page.findAllWithCriteria({ types: ["COMPONENT", "COMPONENT_SET"] })
  .filter(n => n.type === "COMPONENT_SET" ||
    (n.type === "COMPONENT" && n.parent?.type !== "COMPONENT_SET"))
  .filter(n => !/(^|[ /])(?:Archive|Legacy|Deprecated|Scratch)(?:[ /]|$)/i.test(n.name))
  .filter(n => CANONICAL_MASTER_IDS.length === 0 || CANONICAL_MASTER_IDS.includes(n.id));

const metrics = {
  masters: masters.length, ownedLayers: 0,
  semanticColors: 0, componentColors: 0, exceptions: 0,
  wrongCollection: 0, rawColors: 0, paintStylesForReview: 0,
  unresolvedColors: 0, text: 0, unstyledText: 0,
  nonzeroSpacing: 0, boundSpacing: 0, unboundScaleSpacing: 0,
  localSpacingForReview: 0,
  nonzeroRadius: 0, boundRadius: 0, deprecatedRadius: 0,
  rawRadiusForReview: 0
};
const examples = [];
function record(kind, priority, node, property, value, masterName) {
  if (examples.length < 50) examples.push({
    kind, priority, nodeId: node.id, nodeName: node.name,
    property, value, sourceMaster: masterName
  });
}
for (const master of masters) {
  const stack = [master];
  while (stack.length) {
    const n = stack.pop();
    // Instances and their internals belong to an upstream component source.
    // Excluding only children still counts instance-wrapper overrides as owned.
    if (n.type === "INSTANCE") continue;
    metrics.ownedLayers++;
    const bind = n.boundVariables || {};
    // The COMPONENT_SET shell decorates the variants on the Figma canvas;
    // its border/fill is not part of a consumable component instance.
    if (n.type !== "COMPONENT_SET") {
    for (const pair of [["fills", "fillStyleId"], ["strokes", "strokeStyleId"]]) {
      const prop = pair[0], styleProp = pair[1];
      if (!Array.isArray(n[prop])) continue;
      for (const paint of n[prop]) {
        if (paint.type !== "SOLID" || paint.visible === false) continue;
        const id = paint.boundVariables?.color?.id;
        const v = variableById.get(id);
        if (v) {
          const c = collectionById.get(v.variableCollectionId);
          if (c === "03 Semantic") metrics.semanticColors++;
          else if (c === "04 Component Tokens") {
            metrics.componentColors++;
            if (!master.name.startsWith("Tag"))
              record("Component token owner review", "review", n, prop, v.name, master.name);
          } else if (c === "01 Primitives" &&
                     v.name === "palette/bw/white" && master.name.startsWith("Toggle")) {
            metrics.exceptions++;
          } else {
            metrics.wrongCollection++;
            record("Internal or primitive color binding", "P1", n, prop,
              c + " / " + v.name, master.name);
          }
        } else if (id) {
          metrics.unresolvedColors++;
          record("External/unresolved color binding", "review", n, prop, id, master.name);
        } else if (typeof n[styleProp] === "string" && n[styleProp]) {
          metrics.paintStylesForReview++;
          record("Legacy paint style review", "P2", n, prop, n[styleProp], master.name);
        } else {
          metrics.rawColors++;
          record("Raw color", "P1", n, prop, "unbound", master.name);
        }
      }
    }
    }
    if (n.type === "TEXT") {
      metrics.text++;
      if (!n.textStyleId || n.textStyleId === figma.mixed) {
        metrics.unstyledText++;
        record("Text Style missing", "review", n, "textStyleId",
          n.characters?.slice(0, 35), master.name);
      }
    }
    // Component Set auto-layout arranges the Figma variant matrix, not product UI.
    if (n.type !== "COMPONENT_SET" && n.layoutMode && n.layoutMode !== "NONE") {
      for (const prop of ["paddingTop", "paddingRight", "paddingBottom",
                          "paddingLeft", "itemSpacing"]) {
        const value = n[prop];
        if (typeof value !== "number" || value <= 0) continue;
        // A positive itemSpacing on a single-child icon/wrapper frame cannot
        // separate siblings. It is inert geometry, not active spacing debt.
        if (prop === "itemSpacing" && "children" in n && n.children.length < 2 && n.layoutWrap !== "WRAP") continue;
        metrics.nonzeroSpacing++;
        const v = variableById.get(bind[prop]?.id);
        if (v && collectionById.get(v.variableCollectionId) === "Spacing") {
          metrics.boundSpacing++;
        } else if (spacingValues.has(value)) {
          metrics.unboundScaleSpacing++;
          record("Scale spacing without variable", "P2", n, prop, value, master.name);
        } else {
          metrics.localSpacingForReview++;
          record("Local optical spacing review", "review", n, prop, value, master.name);
        }
      }
    }
    if (n.type !== "COMPONENT_SET" &&
        typeof n.cornerRadius === "number" && n.cornerRadius > 0) {
      metrics.nonzeroRadius++;
      const keys = ["topLeftRadius", "topRightRadius",
                    "bottomLeftRadius", "bottomRightRadius"];
      const rv = keys.map(k => variableById.get(bind[k]?.id)).find(Boolean);
      if (rv) {
        metrics.boundRadius++;
        if (rv.name.startsWith("Deprecated")) {
          metrics.deprecatedRadius++;
          record("Deprecated radius", "P1", n, "radius", rv.name, master.name);
        }
      } else {
        metrics.rawRadiusForReview++;
        record("Raw radius / exception review", "review", n,
          "cornerRadius", n.cornerRadius, master.name);
      }
    }
    // Borrowed instance children belong to their upstream component, not this source.
    if ("children" in n && n.type !== "INSTANCE") stack.push(...n.children);
  }
}
return {
  page: page.name, pageId: page.id, metrics, examples,
  limits: [
    "Semantic role correctness, focus and contrast require human review.",
    "Local component geometry and approved exceptions need context.",
    "Nested instances are excluded from owned-source counts.",
    "This is Figma authoring QA only; no Angular/Storybook certification."
  ]
};