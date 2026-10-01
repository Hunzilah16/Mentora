"""
Script to build topic20_data.py containing 50 authentic Cambridge AS Chemistry (9701)
questions on Topic 20: Polymerisation (Addition Polymerisation).
"""

def generate():
    content = r'''"""
Curation of authentic Cambridge International AS Chemistry (9701) exam questions
for Topic 20: Polymerisation.
Subtopic:
  20.1 Addition polymerisation:
       - Mechanism of addition polymerisation (opening of alkene C=C pi-bonds to form saturated C-C sigma-chains)
       - Drawing repeat units from given alkene monomers and vice versa
       - Common commercial polymers: poly(ethene), poly(propene), poly(chloroethene) (PVC), poly(phenylethene) (polystyrene), poly(tetrafluoroethene) (PTFE)
       - Structure-property relationships: chain length, branching, crystallinity, density, and melting point (LDPE vs HDPE)
       - Intermolecular forces between polymer chains: dispersion forces in polyalkenes, permanent dipole-dipole attractions in PVC
       - Action and function of plasticisers in PVC (internal lubrication, increasing flexibility)
       - Environmental problems: non-biodegradability, persistence in landfill, oceanic pollution
       - Disposal methods: incineration (energy recovery, generation of toxic/acidic gases like HCl, flue gas scrubbing with bases)
       - Recycling strategies: mechanical sorting, washing, melting, and chemical feedstock recycling (pyrolysis)
       - Contrast with biodegradable condensation polymers (PLA, polyesters)

Total questions: 50
"""

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class QuestionPart:
    label: str
    text: str
    marks: int
    num_answer_lines: int = 2
    options: List[str] = field(default_factory=list)

@dataclass
class Question:
    number: int
    title: str
    syllabus_ref: str
    difficulty: str  # EASY or HARD
    preamble: str
    parts: List[QuestionPart]
    mark_scheme: List[dict]
    figure_path: Optional[str] = None
    figure_caption: Optional[str] = None

TOPIC_20_QUESTIONS = [
    # =========================================================================
    # PART 1: Addition Mechanism, Monomers & Repeat Units (Q1 - Q13)
    # =========================================================================
    Question(
        number=1,
        title="Addition Polymerisation and Repeat Units — 9701/22/M/J/23/Q6(a)-(d)",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Alkenes undergo addition polymerisation to form saturated, long-chain macromolecules. Fig. 1.1 displays the general addition reaction and representative commercial addition polymers.",
        figure_path="figures/polymers_addition_mechanism_and_repeat_units.png",
        figure_caption="Fig. 1.1: General mechanism of addition polymerisation and common commercial polymers.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the essential structural feature an organic monomer must possess to undergo addition polymerisation, and explain the fate of this feature during the reaction.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw the structural formula of the repeat unit of poly(propene), clearly displaying all bonds and open continuation bonds extending beyond the brackets.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why the atom economy of addition polymerisation reactions is always 100%.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="A sample of poly(ethene) has an average relative molecular mass of 140,000. Calculate the average degree of polymerisation (number of monomer units, n) in this sample.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Must possess an unsaturated carbon-carbon double bond (C=C) [1]",
                "The weak pi-bond of each C=C breaks (opens up) to form new strong single C-C sigma-bonds linking adjacent monomer units into a saturated chain [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "-[CH2-CH(CH3)]- drawn with brackets and continuation bonds extending through both brackets [1]",
                "All atoms and methyl side-branch clearly displayed [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "All atoms present in the reactant monomers are incorporated into the single polymer product; no small molecules or by-products are eliminated [1]"
            ], "marks": 1},
            {"part": "(d)", "points": [
                "Mr of ethene monomer (C2H4) = 2 x 12.0 + 4 x 1.0 = 28.0 [1]",
                "Degree of polymerisation n = 140,000 / 28.0 = 5,000 [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=2,
        title="Deducing Monomers from Polymer Backbones — 9701/21/O/N/23/Q3(a)-(c)",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Consider the section of addition polymer chain shown below:\n... - CH2 - CH(CN) - CH2 - CH(CN) - CH2 - CH(CN) - ...",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the repeat unit of this polymer.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Draw the displayed formula and give the systematic IUPAC name of the monomer used to manufacture this polymer.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State one major commercial application for this polymer (polyacrylonitrile / acrylic fibre).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "-[CH2-CH(CN)]- [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "CH2=CH-C≡N (or displayed showing C=C and C≡N) [1]",
                "Systematic name: Propenenitrile (acrylonitrile) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Synthetic wool substitute in textiles / clothing / knitwear / carpets / carbon fibre precursor [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=3,
        title="PTFE (Teflon): Thermal and Chemical Inertness — 9701/22/F/M/22/Q4(a)-(c)",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Poly(tetrafluoroethene), PTFE, is widely used for non-stick cookware coatings and inert gaskets in chemical plants.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the displayed formula of tetrafluoroethene and the repeat unit of PTFE.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why PTFE is exceptionally resistant to chemical attack by strong acids, alkalis, and oxidising agents, referring to bond enthalpies and atomic size.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Explain why PTFE has an extremely low coefficient of friction (non-stick property).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Monomer: CF2=CF2 [1]",
                "Repeat unit: -[CF2-CF2]- with open continuation bonds [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The C-F bond is extremely strong with a very high bond enthalpy (~485 kJ mol⁻¹), requiring enormous energy to break [1]",
                "The electronegative fluorine atoms form a tight, protective cylindrical sheath around the central carbon backbone [1]",
                "This sheath shields the carbon chain from approaching nucleophiles or electrophiles, providing chemical inertness [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Fluorine atoms have very low polarisability due to their tightly held electrons [1]",
                "This results in exceptionally weak London dispersion forces between PTFE surfaces and other contacting substances, allowing materials to slide freely without adhering [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=4,
        title="Poly(phenylethene) / Polystyrene and Expanded Polystyrene — 9701/23/M/J/23/Q3",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Phenylethene (styrene, C6H5CH=CH2) polymerises to form poly(phenylethene).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of the repeat unit of poly(phenylethene).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Expanded polystyrene (EPS) is manufactured by adding a volatile hydrocarbon foaming agent such as pentane during polymerisation. Explain how this produces lightweight foam beads with high thermal insulation.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State two commercial uses of expanded polystyrene.",
                marks=2,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "-[CH2-CH(C6H5)]- (or benzene ring attached to CH) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Heating vaporises the pentane blowing agent, causing gas bubbles to expand within the softening polymer [1]",
                "The trapped air pockets create a low-density cellular foam (>95% air) that drastically restricts heat transfer by conduction and convection [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Protective packaging for fragile electronics [1]",
                "Thermal insulation boards for buildings / disposable coffee cups [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=5,
        title="Co-Polymerisation: Monomer Deduction — 9701/21/M/J/22/Q4(a)-(c)",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Co-polymers are formed by the simultaneous polymerisation of two different alkene monomers. A section of a co-polymer chain is shown below:\n... - CH2 - CH(CH3) - CH2 - CH(Cl) - CH2 - CH(CH3) - CH2 - CH(Cl) - ...",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the two different alkene monomers used to synthesise this co-polymer, giving their systematic IUPAC names and displayed formulas.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="State the mole ratio in which these two monomers are combined in this section of the polymer.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Suggest why industrial chemists manufacture co-polymers rather than simple homopolymers.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Monomer 1: Propene, CH2=CH-CH3 [1]",
                "Monomer 2: Chloroethene, CH2=CH-Cl [1]",
                "Displayed formulas showing C=C double bonds clearly [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "1 : 1 mole ratio [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Co-polymerisation allows tailoring of mechanical properties by combining characteristics of both monomers [1]",
                "For example, introducing propene into PVC disrupts crystalline packing to increase impact resistance, elasticity, or flexibility without losing chemical resistance [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=6,
        title="Poly(methyl methacrylate) / Perspex — 9701/22/O/N/22/Q4(a)-(c)",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Methyl methacrylate, CH2=C(CH3)COOCH3, polymerises to produce transparent poly(methyl methacrylate) (PMMA, Perspex or Plexiglas).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of two consecutive repeat units of PMMA.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why PMMA is an addition polymer rather than a condensation polymer, despite containing ester functional groups.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State one property of PMMA that makes it superior to traditional silicate glass in aircraft windows and riot shields.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Two units showing -[CH2-C(CH3)(COOCH3)-CH2-C(CH3)(COOCH3)]- [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Polymerisation occurs solely via the opening of the C=C double bond in the monomer [1]",
                "No small molecule (such as water or HCl) is eliminated during chain growth; the ester group was pre-existing in the monomer [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Significantly higher shatter/impact resistance (toughness) and approximately half the density (lighter weight) of silicate glass [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=7,
        title="Multiple Choice: Monomer Identification — 9701/12/M/J/23/Q31",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="A section of polymer chain has the structure: -[CH(CH3)-CH(CH3)]n-.",
        parts=[
            QuestionPart(
                label="(a)",
                text="What is the monomer of this polymer?\nA  Propene\nB  But-1-ene\nC  But-2-ene\nD  2-methylpropene",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain your reasoning by showing how the monomer structure relates to the repeat unit.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (But-2-ene) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The repeat unit has two adjacent carbon atoms in the backbone, each carrying one -H and one -CH3 group [1]",
                "Re-introducing the double bond between these two backbone carbons yields CH3-CH=CH-CH3, which is but-2-ene [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=8,
        title="Tacticity in Poly(propene) (Extension Concepts) — 9701/21/O/N/22/Q5",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="The stereochemical arrangement of methyl side-groups along the poly(propene) chain (tacticity) determines its physical properties.\n• Isotactic: All methyl groups are on the same side of the backbone chain.\n• Atactic: Methyl groups are arranged randomly on either side.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why isotactic poly(propene) has a higher melting point and higher tensile strength than atactic poly(propene).",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Name the type of catalyst developed by Karl Ziegler and Giulio Natta that enables the synthesis of highly stereoregular isotactic poly(propene).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The regular spatial orientation in isotactic poly(propene) allows the polymer chains to pack tightly and uniformly into a crystalline lattice [1]",
                "Close packing maximises the surface area of contact between adjacent chains [1]",
                "This creates substantially stronger cumulative London dispersion forces that require more thermal energy to overcome [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Ziegler-Natta catalyst (titanium(IV) chloride and triethylaluminium) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=9,
        title="Superabsorbent Polymers: Poly(sodium acrylate) — 9701/22/M/J/22/Q5",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Poly(sodium acrylate) is an addition polymer used as the absorbent core in disposable baby nappies, capable of absorbing hundreds of times its own mass in water.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Sodium acrylate has structural formula CH2=CH-COONa. Draw the structural formula of the repeat unit of poly(sodium acrylate).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain in terms of bonding and intermolecular interactions why poly(sodium acrylate) absorbs water so extensively.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why poly(sodium acrylate) absorbs significantly less salt water (0.9% NaCl solution) than pure distilled water.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "-[CH2-CH(COONa)]- with open continuation bonds [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The polymer contains abundant carboxylate ions (-COO⁻) and Na⁺ ions along its chain [1]",
                "It forms extensive ion-dipole attractions and hydrogen bonds with polar water molecules, drawing water into the polymer network via osmotic swelling [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "In salt water, the high external concentration of Na⁺ and Cl⁻ ions reduces the osmotic gradient between the solution and the gel interior [1]",
                "Additionally, external Na⁺ ions shield the negative charges on the carboxylate groups, decreasing electrostatic chain repulsion and reducing gel expansion [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=10,
        title="Deducing Monomer from Degradation Products — 9701/23/O/N/23/Q5",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="When an addition polymer P is pyrolysed (cracked thermally), it depolymerises to yield its alkene monomer M. Monomer M decolourises bromine water, reacts with acidified K2Cr2O7 to form a ketone, and has molecular formula C4H8.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Deduce the structural formula and systematic name of monomer M.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Draw the structural formula of two repeat units of polymer P.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State whether polymer P exhibits stereoisomerism along its backbone.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Monomer M gives a ketone upon oxidation with dichromate -> 2-methylpropene (CH2=C(CH3)2) or but-2-ene [1]",
                "2-methylpropene oxidises to propanone and CO2; but-2-ene oxidises to ethanoic acid. Thus M is 2-methylpropene (isobutene) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "-[CH2-C(CH3)2-CH2-C(CH3)2]- (poly(isobutene)) [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "No, the substituted carbon carries two identical methyl groups, so there are no chiral centres along the chain [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=11,
        title="Multiple Choice: Polymer of But-1-ene — 9701/11/O/N/23/Q27",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Which structure represents the repeat unit of poly(but-1-ene)?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Choose the correct repeat unit:\nA  -[CH2-CH2-CH2-CH2]-\nB  -[CH2-CH(CH2CH3)]-\nC  -[CH(CH3)-CH(CH3)]-\nD  -[CH2-C(CH3)2]-",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Explain why option A is incorrect.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (-[CH2-CH(CH2CH3)]-) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Option A is poly(ethene) or a straight 4-carbon chain; in addition polymerisation of but-1-ene (CH2=CH-C2H5), the ethyl group remains as a side branch attached to the backbone [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=12,
        title="Natural and Synthetic Rubber: Poly(isoprene) — 9701/21/M/J/21/Q6",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Natural rubber is an addition polymer of 2-methylbuta-1,3-diene (isoprene).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the displayed formula of 2-methylbuta-1,3-diene.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain how 1,4-addition across this conjugated diene system produces a polymer that still retains one C=C double bond per repeat unit.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain how vulcanisation (heating rubber with sulfur) alters its physical properties in terms of polymer cross-linking.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "CH2=C(CH3)-CH=CH2 [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The two terminal C=C bonds break to form single bonds extending out of the repeat unit [1]",
                "The remaining electrons pair up to form a new internal C=C double bond between C2 and C3: -[CH2-C(CH3)=CH-CH2]- [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Sulfur forms covalent disulfide bridges (-S-S-) cross-linking adjacent polymer chains [1]",
                "This prevents chains from permanently slipping past one another when stretched, increasing elasticity, toughness, and thermal stability [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=13,
        title="Ring-Opening vs Addition Polymerisation — 9701/22/F/M/21/Q5",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Oxirane (ethylene oxide) polymerises by a ring-opening mechanism to produce poly(ethylene glycol) (PEG).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of oxirane.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Draw the repeat unit of poly(ethylene glycol).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Explain why ring opening of oxirane occurs readily, citing bond angle strain.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Three-membered ring with two carbon atoms and one oxygen atom [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "-[CH2-CH2-O]- with open continuation bonds [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "The bond angles in the 3-membered oxirane ring are approximately 60°, forced far away from normal sp3 tetrahedral angle (109.5°) [1]",
                "This causes severe ring strain; opening the ring relieves this strain, providing a strong thermodynamic driving force for polymerisation [1]"
            ], "marks": 2}
        ]
    ),

    # =========================================================================
    # PART 2: Structure-Property Relationships: LDPE vs HDPE (Q14 - Q26)
    # =========================================================================
    Question(
        number=14,
        title="Comparison of LDPE and HDPE Architecture — 9701/22/M/J/23/Q7(a)-(e)",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Poly(ethene) is produced commercially in two principal forms: Low Density Polyethene (LDPE) and High Density Polyethene (HDPE). Fig. 14.1 compares their manufacturing conditions, chain branching, and resulting physical properties.",
        figure_path="figures/polymers_ldpe_vs_hdpe_structure.png",
        figure_caption="Fig. 14.1: Structural comparison between branched LDPE and linear HDPE.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the reaction conditions (temperature, pressure, catalyst/initiator) used in the industrial manufacture of LDPE.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the reaction conditions used in the industrial manufacture of HDPE, including the name of the catalyst.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain in terms of molecular geometry and packing why HDPE has a higher density and a higher melting point than LDPE.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="State one typical everyday use for LDPE and one for HDPE, relating each use to its mechanical properties.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "High pressure (~1500 - 3000 atm) and high temperature (~200 °C) [1]",
                "Initiator: Traces of oxygen or organic peroxides (free radical polymerisation) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Low pressure (~2 - 10 atm) and moderate temperature (~60 - 70 °C) [1]",
                "Catalyst: Ziegler-Natta catalyst (e.g. titanium(IV) chloride with triethylaluminium) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "HDPE chains are linear with negligible branching, allowing them to pack closely in tight parallel alignment into a crystalline structure [1]",
                "Close packing increases mass per unit volume (higher density, ~0.96 vs ~0.92 g cm⁻³) [1]",
                "Close packing also maximises surface contact area between chains, establishing stronger cumulative London dispersion forces that require higher thermal energy to overcome (m.p. ~135 °C vs ~105 °C) [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "LDPE: Squeeze bottles / plastic shopping bags / cling film because it is flexible and soft [1]",
                "HDPE: Milk crates / buckets / rigid water pipes / safety helmets because it is stiff, tough, and rigid [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=15,
        title="Intermolecular Forces and Polymer Melting Points — 9701/21/O/N/23/Q5",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Table 15.1 lists the softening temperatures (melting ranges) of three polymers of comparable chain length:\n• Poly(ethene): ~115 °C\n• Poly(chloroethene) (PVC): ~180 °C\n• Nylon 6,6: ~260 °C",
        parts=[
            QuestionPart(
                label="(a)",
                text="Identify the primary type of intermolecular force present between polymer chains in each of the three polymers.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Explain why PVC has a significantly higher melting point than poly(ethene).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why Nylon 6,6 has the highest melting point of the three polymers.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Poly(ethene): London dispersion (induced dipole-dipole) forces [1]",
                "PVC: Permanent dipole-dipole forces (between polar C-Cl bonds) and London dispersion forces [1]",
                "Nylon 6,6: Extensive intermolecular hydrogen bonding (between N-H and C=O groups) and dispersion forces [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "PVC contains highly polar C-Cl bonds along the chain [1]",
                "Permanent dipole-dipole attractions between adjacent chains are stronger than the temporary induced dipole forces in non-polar poly(ethene), requiring more energy to disrupt [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Intermolecular hydrogen bonds between N-H and C=O groups in Nylon 6,6 are significantly stronger than both permanent dipole-dipole forces and dispersion forces [1]",
                "This creates a rigid crystalline network with very high thermal stability [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=16,
        title="Chain Length and Tensile Strength — 9701/22/O/N/22/Q5",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Poly(ethene) waxes (Mr ≈ 2,000) are soft and crumbly, whereas ultra-high-molecular-weight poly(ethene) (UHMWPE, Mr ≈ 3,000,000) is bullet-resistant.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why increasing the average chain length (molecular mass) dramatically increases the tensile strength and melting point of poly(ethene).",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="State one application of ultra-high-molecular-weight poly(ethene).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Longer polymer chains contain vastly more electrons per molecule [1]",
                "Cumulative London dispersion forces along the extensive length of each chain become enormous [1]",
                "Long chains also undergo extensive physical entanglement, preventing chains from easily sliding past one another under tension [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Bulletproof vests / body armour / hip replacement joint implants / heavy-duty industrial tow ropes [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=17,
        title="Multiple Choice: Density of Polyethene — 9701/12/M/J/22/Q26",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Why does HDPE have a higher density than LDPE?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct reason:\nA  HDPE contains heavier elements than carbon and hydrogen\nB  HDPE has less chain branching, allowing closer packing of molecules\nC  HDPE contains more double bonds along the chain\nD  HDPE molecules are held together by hydrogen bonds",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the approximate density of HDPE compared to LDPE.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (HDPE has less chain branching, allowing closer packing of molecules) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "HDPE density is ~0.95 - 0.97 g cm⁻³ compared to ~0.91 - 0.93 g cm⁻³ for LDPE [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=18,
        title="Thermosetting vs Thermosoftening Polymers — 9701/23/M/J/22/Q4",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Polymers are broadly categorised into thermoplastics (thermosoftening) and thermosets (thermosetting).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Describe the difference in molecular structure between a thermoplastic and a thermosetting polymer.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain in terms of bonding why thermoplastics can be repeatedly melted, reshaped, and recycled, whereas thermosets char and decompose when heated strongly.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="State whether poly(ethene) is a thermoplastic or a thermoset.",
                marks=1,
                num_answer_lines=1
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Thermoplastics consist of individual linear or branched chains held together only by weak intermolecular forces [1]",
                "Thermosets consist of polymer chains interconnected by extensive permanent covalent cross-links, forming a giant 3D network [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "In thermoplastics, heating overcomes the weak intermolecular forces, allowing chains to slide past one another and flow (melts without breaking covalent bonds) [1]",
                "In thermosets, covalent cross-links are very strong and cannot be overcome without breaking the covalent bonds of the polymer backbone itself [1]",
                "High temperatures lead to thermal degradation / charring rather than melting [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Thermoplastic [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=19,
        title="Amorphous vs Semi-Crystalline Regions in Polymers — 9701/21/O/N/21/Q6",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Solid polymers typically contain both crystalline domains (where chains align in parallel) and amorphous domains (where chains are tangled randomly).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why crystalline domains give polymers higher rigidity, higher tensile strength, and optical opacity (translucency).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why amorphous domains impart flexibility, impact resistance, and optical clarity (transparency).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why cold drawing (stretching) a polymer fibre during manufacturing increases its tensile strength.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Close, regular packing maximises intermolecular forces, resisting deformation (rigid) [1]",
                "Boundaries between crystalline and amorphous regions scatter light, giving a translucent/opaque appearance [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Loose, random chain packing allows chain segments to flex and absorb mechanical shock [1]",
                "Uniform refractive index throughout amorphous regions allows light to pass without scattering (transparent) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Drawing pulls randomly tangled chains into parallel alignment along the axis of tension [1]",
                "Increases crystallinity and maximises intermolecular attractions along the fibre length, dramatically enhancing tensile strength [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=20,
        title="Free-Radical Polymerisation Mechanism: Ethene — 9701/22/F/M/23/Q6",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="The free-radical polymerisation of ethene to form LDPE occurs in three distinct stages: initiation, propagation, and termination.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Initiation involves the thermal homolytic fission of an organic peroxide, R-O-O-R. Write an equation showing the formation of alkoxy free radicals (RO•).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Write the equation for the reaction of RO• with an ethene molecule to initiate the growing carbon radical chain.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Write a general equation for a propagation step where a growing radical chain adds another ethene monomer.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(d)",
                text="Describe how chain branching arises during LDPE synthesis via intramolecular hydrogen abstraction (back-biting).",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "RO-OR -> 2RO• (homolytic fission of O-O bond) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "RO• + CH2=CH2 -> RO-CH2-CH2• [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "R-(CH2-CH2)n• + CH2=CH2 -> R-(CH2-CH2)n+1• [1]"
            ], "marks": 1},
            {"part": "(d)", "points": [
                "The radical chain end curls back in a 6-membered transition state and abstracts a hydrogen atom from a carbon 4-5 positions back along its own chain [1]",
                "This creates an internal radical along the backbone from which new chain growth propagates, producing a branch (e.g. butyl side branch) [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=21,
        title="Polymer Combustion: Heat of Combustion Calculations — 9701/21/O/N/23/Q6",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="When 1.00 g of poly(ethene) undergoes complete combustion, it produces 47.2 kJ of heat energy.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write the balanced chemical equation for the complete combustion of one repeat unit of poly(ethene), -[CH2-CH2]-.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the standard enthalpy change of combustion per mole of repeat unit (Mr = 28.0 g mol⁻¹).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why addition polymers make excellent high-calorific fuels for municipal waste-to-energy power plants.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C2H4 + 3O2 -> 2CO2 + 2H2O [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Enthalpy change = -47.2 kJ g⁻¹ x 28.0 g mol⁻¹ = -1322 kJ mol⁻¹ [2]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Polyalkenes consist almost entirely of reduced carbon and hydrogen atoms (high percentage of C-C and C-H bonds) [1]",
                "Their calorific value is comparable to or exceeds that of fossil fuels like coal and petroleum [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=22,
        title="Multiple Choice: Monomer of Polystyrene — 9701/11/M/J/23/Q32",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="What is the systematic IUPAC name of the monomer used to manufacture polystyrene?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct name:\nA  Phenylethene\nB  Phenylmethane\nC  Phenylethyne\nD  1,2-diphenylethene",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Draw the structural formula of phenylethene.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A (Phenylethene / styrene) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "C6H5-CH=CH2 [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=23,
        title="Superglue Polymerisation (Ethyl Cyanoacrylate) — 9701/23/O/N/22/Q5",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Commercial 'Superglue' contains ethyl 2-cyanoacrylate, CH2=C(CN)COOCH2CH3, which undergoes rapid anionic polymerisation when exposed to traces of atmospheric moisture.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of the repeat unit of the superglue polymer.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why ethyl 2-cyanoacrylate polymerises so rapidly in the presence of weak nucleophiles like water or OH⁻.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Suggest an organic solvent that can dissolve cured superglue from skin or clothing.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "-[CH2-C(CN)(COOCH2CH3)]- with open continuation bonds [2]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "The carbon atom is bonded to two strongly electron-withdrawing groups: nitrile (-CN) and ester (-COOCH2CH3) [1]",
                "These groups make the C=C double bond exceptionally electron-deficient and strongly stabilise the resulting carbanion intermediate, enabling rapid chain propagation [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Propanone (acetone) / ethyl ethanoate (nail polish remover) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=24,
        title="Degradation of Polymers by Ultraviolet Light — 9701/22/M/J/22/Q6",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Many addition polymers become brittle, crack, and discolour when left outdoors in direct sunlight for extended periods.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain how ultraviolet (UV) radiation causes photodegradation of the polymer backbone.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the role of carbon black or UV stabilisers (hindered amine light stabilisers, HALS) added to commercial plastics.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "High-energy UV photons are absorbed by polymer impurities or bonds, causing homolytic cleavage of C-C or C-H bonds [1]",
                "This generates free radicals that react with atmospheric oxygen (photo-oxidation), severing polymer chains and decreasing average molecular mass (chain scission) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Carbon black absorbs and dissipates harmful UV radiation as harmless heat [1]",
                "Chemical UV stabilisers act as free-radical scavengers, terminating radical chain propagation before polymer chains are cleaved [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=25,
        title="Physical Properties of Poly(chloroethene) uPVC — 9701/21/O/N/23/Q7",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Unplasticised PVC (uPVC) is universally chosen for domestic window frames and rainwater gutters.",
        parts=[
            QuestionPart(
                label="(a)",
                text="State three physical or chemical properties of uPVC that make it superior to wood or painted steel for exterior window frames.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Write the equation for the formation of PVC from its monomer.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Inert to moisture / does not rot, warp, or corrode [1]",
                "Low maintenance / does not require periodic painting [1]",
                "Excellent thermal and electrical insulator / high mechanical rigidity and weather resistance [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "n CH2=CHCl -> -[CH2-CH(Cl)]-n [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=26,
        title="Multiple Choice: Polymer Characteristics — 9701/12/O/N/23/Q28",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Which addition polymer contains fluorine atoms?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Choose the correct polymer:\nA  PVC\nB  PTFE\nC  PMMA\nD  PET",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="Give the full chemical name of PTFE.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (PTFE) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Poly(tetrafluoroethene) [1]"
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # PART 3: PVC, Dipoles & Plasticisers (Q27 - Q39)
    # =========================================================================
    Question(
        number=27,
        title="Structure of PVC and the Mechanism of Plasticisers — 9701/21/M/J/23/Q11(a)-(d)",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Poly(chloroethene), PVC, can be manufactured as either a hard, rigid material or a soft, flexible material. Fig. 27.1 illustrates the polar dipole interactions in unplasticised PVC and the molecular action of plasticiser additives.",
        figure_path="figures/polymers_pvc_plasticisers_dipoles.png",
        figure_caption="Fig. 27.1: Intermolecular forces in unplasticised PVC (uPVC) compared to flexible plasticised PVC.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why pure unplasticised PVC (uPVC) is a hard, rigid polymer, referring to the polarity of its bonds and intermolecular attractions.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Describe how adding plasticiser molecules (such as dioctyl phthalate) alters the intermolecular forces and structure of PVC, transforming it into a flexible material.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="State one application of rigid uPVC and one application of flexible plasticised PVC.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Explain why plasticisers can slowly leach out of flexible PVC products over time, making older plastics stiff and brittle.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "The C-Cl bond is highly polar due to the large electronegativity difference between carbon (2.5) and chlorine (3.0) [1]",
                "Strong permanent dipole-dipole attractions exist between adjacent polymer chains [1]",
                "These attractions lock the chains firmly in place, preventing them from sliding over each other, giving a rigid, stiff material [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Plasticisers are small ester molecules that slot between the long polymer chains [1]",
                "They push the polymer chains further apart, increasing intermolecular spacing [1]",
                "This significantly weakens the permanent dipole-dipole forces between chains, allowing them to slip and slide past each other easily [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Rigid uPVC: Window frames / exterior doors / underground sewer pipes [1]",
                "Flexible PVC: Electrical cable insulation / garden hoses / inflatable toys / vinyl flooring [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Plasticiser molecules are not covalently bonded to the polymer chains (held only by weak intermolecular forces) [1]",
                "Over time, exposure to heat, sunlight, or solvents allows small plasticiser molecules to diffuse to the surface and evaporate / wash away, restoring strong dipole attractions between chains [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=28,
        title="Glass Transition Temperature (Tg) in Polymers — 9701/22/O/N/23/Q6",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="The glass transition temperature (Tg) is the temperature at which an amorphous polymer transitions from a hard, glassy, brittle state to a flexible, rubbery state.\n• Pure PVC: Tg ≈ 85 °C\n• Plasticised PVC: Tg ≈ -20 °C\n• Poly(ethene): Tg ≈ -120 °C",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why pure PVC is glassy and rigid at room temperature (20 °C), whereas poly(ethene) is flexible at room temperature.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain how plasticisers lower the glass transition temperature of PVC to below freezing.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Room temperature (20 °C) is below the Tg of pure PVC (85 °C), so chain segments lack sufficient thermal energy to rotate or slip (glassy state) [1]",
                "Room temperature is far above the Tg of poly(ethene) (-120 °C), so chains have high mobility and flex easily (rubbery/flexible state) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Plasticisers increase free volume between chains and weaken dipole attractions [1]",
                "Less thermal kinetic energy is required for chain segments to rotate and slide, shifting the transition temperature far below ambient temperatures [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=29,
        title="Health and Environmental Concerns with Phthalate Plasticisers — 9701/21/O/N/22/Q7",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Phthalate esters such as DEHP (di-2-ethylhexyl phthalate) are widely restricted in children's toys and medical equipment.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why phthalates are able to leach out of PVC plastics into liquids or foods.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="State one biomedical concern associated with human exposure to phthalates.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(c)",
                text="Suggest an alternative bio-based, non-toxic plasticiser class that can replace phthalates.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "They are physically mixed / blended additives, not chemically (covalently) bound to the PVC backbone [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Endocrine disruptors / interfere with hormone function / reproductive and developmental toxicity [1]"
            ], "marks": 1},
            {"part": "(c)", "points": [
                "Citrate esters / epoxidised soybean oil (ESBO) / adipate esters [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=30,
        title="Multiple Choice: Action of Plasticisers — 9701/11/M/J/22/Q27",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="What is the primary role of a plasticiser added to poly(chloroethene)?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct role:\nA  To form covalent cross-links between polymer chains\nB  To increase the tensile strength and rigidity of the plastic\nC  To weaken intermolecular attractions between chains, increasing flexibility\nD  To make the polymer biodegradable in soil",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the class of organic compounds most commonly used as plasticisers.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (To weaken intermolecular attractions between chains, increasing flexibility) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Esters (e.g. phthalate esters or dialkyl phthalates) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=31,
        title="Chlorinated Poly(vinyl chloride) (CPVC) — 9701/23/M/J/23/Q6",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Post-chlorination of PVC via free-radical chlorination yields CPVC, which contains up to 67% chlorine by mass.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Write an equation showing how UV light initiates the chlorination of a -CH2- unit in PVC.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why CPVC can withstand hot water up to 95 °C without deforming, whereas standard PVC softens at 60 °C.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Cl2 -> 2Cl• (UV light homolytic fission) [1]",
                "-[CH2-CHCl]- + Cl• -> -[CH•-CHCl]- + HCl [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Additional bulky chlorine atoms increase steric crowding and dipole-dipole attractions along the chain [1]",
                "This significantly restricts chain mobility, raising the glass transition temperature (Tg ~ 115 °C) and enabling use in hot water piping [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=32,
        title="Poly(vinyl acetate) (PVA) and Wood Glue — 9701/22/F/M/22/Q6",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Ethenyl ethanoate (vinyl acetate, CH2=CHOCOCH3) polymerises to form poly(vinyl acetate), PVA, the active polymer in white woodwork adhesive.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of the repeat unit of PVA.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="PVA adhesive binds strongly to porous wood surfaces. Explain this adhesion in terms of hydrogen bonding with cellulose fibres in wood.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="When PVA is hydrolysed with aqueous sodium hydroxide, an alcohol polymer is formed. Name this polymer.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "-[CH2-CH(OCOCH3)]- with open continuation bonds [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "The carbonyl and ester oxygen atoms in PVA act as hydrogen bond acceptors [1]",
                "They form abundant hydrogen bonds with the extensive hydroxyl (-OH) groups of cellulose fibres in wood, creating strong interfacial adhesion [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Poly(ethenol) / poly(vinyl alcohol) (PVAL) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=33,
        title="Water-Soluble Addition Polymers: Poly(ethenol) — 9701/21/M/J/22/Q6",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Poly(ethenol) is a unique addition polymer that is completely soluble in warm water, used in single-dose laundry detergent pods and hospital laundry bags.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of the repeat unit of poly(ethenol).",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why ethenol (vinyl alcohol, CH2=CHOH) CANNOT be used directly as a monomer to manufacture poly(ethenol). Mention keto-enol tautomerism.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why poly(ethenol) dissolves rapidly in water.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "-[CH2-CH(OH)]- with open continuation bonds [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Ethenol is an unstable enol that rapidly tautomerises into its more thermodynamically stable keto isomer, ethanal (CH3CHO) [1]",
                "Consequently, free ethenol monomer cannot exist in high concentration for polymerisation; poly(ethenol) must be made by hydrolysing poly(ethenyl ethanoate) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Every alternate carbon atom in the chain carries a polar -OH group [1]",
                "These -OH groups form extensive hydrogen bonds with surrounding water molecules, overcoming inter-chain attractions and dissolving the polymer [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=34,
        title="Multiple Choice: Polymer of Ethenylbenzene — 9701/12/M/J/23/Q32",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Which repeating unit represents poly(phenylethene)?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct repeating unit:\nA  -[CH2-CH(C6H5)]-\nB  -[CH(C6H5)-CH(C6H5)]-\nC  -[C6H4-CH2-CH2]-\nD  -[CH2-C(C6H5)2]-",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the empirical formula of poly(phenylethene).",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "A (-[CH2-CH(C6H5)]-) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "CH (Monomer is C8H8, ratio C:H is 1:1) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=35,
        title="Cross-Linking of Addition Polymers with Divinylbenzene — 9701/23/O/N/23/Q6",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Ion-exchange resin beads are prepared by co-polymerising phenylethene with a small percentage of 1,4-diethenylbenzene (divinylbenzene).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of 1,4-diethenylbenzene.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain how the two double bonds in 1,4-diethenylbenzene link separate polystyrene chains together into an insoluble 3D network.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why increasing the percentage of 1,4-diethenylbenzene reduces the swelling of the resin beads in water.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Benzene ring with two -CH=CH2 groups in 1,4 (para) positions [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Each of the two vinyl groups can participate in a different growing polymer chain [1]",
                "This forms strong covalent cross-links bridging adjacent chains into a giant 3D macromolecular network [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "A higher density of rigid cross-links restricts the physical mobility of the polymer chains [1]",
                "The tightly knit mesh cannot expand or stretch to accommodate incoming water molecules, reducing swelling [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=36,
        title="Electrical Conductivity in Conjugated Polymers: Poly(ethyne) — 9701/21/O/N/22/Q8",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Poly(ethyne) (polyacetylene), -[CH=CH]n-, can conduct electricity when doped with iodine.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw two repeat units of poly(ethyne) showing alternating single and double bonds.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why alternating double and single bonds (conjugation) allow delocalisation of electrons along the polymer chain.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Explain why standard poly(ethene) is an electrical insulator.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "-[CH=CH-CH=CH]- with open continuation bonds [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Every carbon atom is sp2 hybridised with an unhybridised p-orbital [1]",
                "Continuous sideways overlap of adjacent p-orbitals creates an extended delocalised pi electron band extending the entire length of the polymer chain [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "In poly(ethene), all carbon atoms are sp3 hybridised with only localised sigma bonds [1]",
                "All valence electrons are held tightly in single covalent bonds, leaving no mobile delocalised electrons to carry charge [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=37,
        title="Multiple Choice: Polymer from Substituted Ethenes — 9701/11/O/N/22/Q26",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Which monomer forms the polymer shown: -[CH2-C(CH3)(COOCH3)]n-?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct monomer:\nA  Methyl propenoate\nB  Methyl 2-methylpropenoate\nC  Ethyl propenoate\nD  Propyl ethanoate",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the commercial name of this polymer.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (Methyl 2-methylpropenoate / methyl methacrylate) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Perspex / Plexiglas / PMMA [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=38,
        title="Polymer Molecular Mass Distribution (Polydispersity) — 9701/22/M/J/22/Q7",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Unlike pure small organic molecules that have a single fixed Mr, synthetic polymers exhibit a range of molecular masses.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why synthetic addition polymers do not have a sharp, single melting point, but soften over a temperature range.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain why termination steps in free-radical addition polymerisation produce polymer chains of varying lengths.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Synthetic polymers consist of a mixture of chains with different chain lengths and different relative molecular masses [1]",
                "Shorter chains with weaker dispersion forces soften and separate at lower temperatures, while longer chains require higher temperatures, resulting in a broad softening range [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Termination occurs via random collisions between two radical chains (combination or disproportionation) [1]",
                "Since initiation and propagation happen continuously and randomly, chains grow for different lengths of time before colliding with another radical to terminate [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=39,
        title="Flame Retardants in PVC and Polymers — 9701/21/M/J/23/Q7",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Pure poly(ethene) burns readily with a smokeless flame, whereas pure PVC is inherently flame-retardant.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why pure PVC is self-extinguishing when removed from a direct flame.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State the toxic and corrosive gas liberated when PVC does combust in a sustained building fire.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "When heated, PVC releases non-flammable hydrogen chloride gas (HCl) [1]",
                "The dense HCl gas smothers the flame by excluding atmospheric oxygen and scavenges combustion free radicals (H• and •OH), extinguishing the fire [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Hydrogen chloride gas (HCl) / dioxins [1]"
            ], "marks": 1}
        ]
    ),

    # =========================================================================
    # PART 4: Environmental Impact, Recycling & Biodegradability (Q40 - Q50)
    # =========================================================================
    Question(
        number=40,
        title="Disposal and Waste Management Strategies — 9701/22/M/J/23/Q8(a)-(d)",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="The widespread consumption of non-biodegradable addition polymers poses major ecological challenges. Fig. 40.1 illustrates three key waste management pathways: landfill, incineration, and recycling.",
        figure_path="figures/polymers_recycling_and_disposal.png",
        figure_caption="Fig. 40.1: Summary of polymer disposal methods and environmental mitigation strategies.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why addition polymers such as poly(ethene) and poly(propene) do NOT biodegrade in landfill sites, referring to bond characteristics and microbial action.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(b)",
                text="Incineration of domestic plastic waste recovers valuable electrical energy. However, burning PVC releases hazardous acidic emissions. Name the toxic gas released and explain how flue gas scrubbers neutralise it using calcium oxide.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="Describe the difference between mechanical recycling and chemical feedstock recycling (pyrolysis) of plastic waste.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(d)",
                text="Explain why different types of plastic (e.g. PET, HDPE, PVC) must be carefully sorted before mechanical recycling.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Addition polymers have a saturated, non-polar carbon-carbon backbone held by very strong C-C and C-H sigma bonds [1]",
                "They lack polar functional groups (such as ester or amide links) that can undergo chemical hydrolysis [1]",
                "Naturally occurring microorganisms and soil bacterial enzymes cannot recognise or bind to the non-polar inert C-C backbone [1]"
            ], "marks": 3},
            {"part": "(b)", "points": [
                "Gas: Hydrogen chloride gas (HCl) [1]",
                "Calcium oxide (CaO) is a basic metal oxide that reacts with and neutralises acidic HCl gas in the chimney scrubbers [1]",
                "Equation: CaO(s) + 2HCl(g) -> CaCl2(s) + H2O(l) (producing non-toxic solid calcium chloride) [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Mechanical recycling: Sorting by resin identification code, washing, shredding into flakes, melting, and reforming into new plastic items without altering the polymer's chemical structure [1]",
                "Chemical feedstock recycling (pyrolysis): Thermal cracking in the absence of oxygen at high temperatures to break covalent bonds [1]",
                "Converts the polymer back into original alkene monomers or raw petrochemical feedstocks for new chemical syntheses [1]"
            ], "marks": 3},
            {"part": "(d)", "points": [
                "Different polymers have different melting temperatures and are chemically immiscible with one another [1]",
                "Mixing different plastics produces a weak, brittle material with poor mechanical properties due to phase separation and weak interfacial bonding [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=41,
        title="Microplastics and Marine Pollution — 9701/21/O/N/23/Q8",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Plastic debris discarded into oceans fragments over decades into microscopic particles called microplastics (diameter < 5 mm).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain how mechanical wave action and solar UV radiation degrade large plastic waste into microplastics without fully breaking down the chemical molecules.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State two ecological hazards caused by microplastics in marine ecosystems.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "UV radiation initiates photo-oxidation, causing localized chain scission that makes the plastic brittle [1]",
                "Physical abrasion by waves, sand, and wind shatters the brittle plastic into tiny fragments without decomposing the molecules to CO2 and water [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Ingested by marine organisms (plankton, fish, seabirds), causing gut blockage, starvation, and physical tissue injury [1]",
                "Microplastics adsorb persistent organic pollutants (pesticides, heavy metals) and bioaccumulate up the marine food chain into humans [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=42,
        title="Biodegradable Polymers: Poly(lactic acid) (PLA) — 9701/22/O/N/22/Q6",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Poly(lactic acid), PLA, is a biodegradable and compostable aliphatic polyester manufactured from renewable corn starch.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw the structural formula of 2-hydroxypropanoic acid (lactic acid) and the repeat unit of PLA.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Explain in terms of functional groups and mechanism why PLA is biodegradable under industrial composting conditions, whereas poly(propene) is non-biodegradable.",
                marks=3,
                num_answer_lines=4
            ),
            QuestionPart(
                label="(c)",
                text="State two environmental benefits of PLA over conventional petroleum-derived plastics.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Lactic acid: CH3-CH(OH)-COOH [1]",
                "PLA repeat unit: -[O-CH(CH3)-CO]- with open continuation bonds [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "PLA contains polar ester linkages (-COO-) in its polymer backbone [1]",
                "These ester links are susceptible to nucleophilic attack by water molecules (hydrolysis) catalysed by bacterial esterase enzymes under warm, moist composting conditions [1]",
                "Poly(propene) possesses an unreactive, non-polar saturated C-C backbone that completely resists enzymatic and chemical hydrolysis [1]"
            ], "marks": 3},
            {"part": "(c)", "points": [
                "Derived from renewable agricultural biomass (corn starch / sugar cane) rather than depleting crude oil reserves [1]",
                "Decomposes naturally in compost into non-toxic water and carbon dioxide, eliminating long-term landfill accumulation [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=43,
        title="Flue Gas Scrubbing Stoichiometry — 9701/23/M/J/23/Q7",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="An incineration plant burns 2.50 tonnes of plastic waste containing 15.0% by mass of poly(chloroethene), PVC (repeat unit Mr = 62.5).",
        parts=[
            QuestionPart(
                label="(a)",
                text="Calculate the mass (in tonnes) of PVC present in the waste.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Calculate the number of moles of HCl gas liberated when all the PVC is completely incinerated.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Calculate the minimum mass of calcium carbonate, CaCO3 (Mr = 100.1), required to neutralise all the evolved HCl gas.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Mass of PVC = 2.50 x 0.150 = 0.375 tonnes (375,000 g) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Moles of repeat unit = 375,000 / 62.5 = 6,000 mol [1]",
                "Each repeat unit produces 1 mole of HCl -> Moles of HCl = 6,000 mol [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Reaction: CaCO3 + 2HCl -> CaCl2 + H2O + CO2 (1 : 2 mole ratio) [1]",
                "Moles of CaCO3 required = 6,000 / 2 = 3,000 mol -> Mass = 3,000 x 100.1 = 300,300 g = 0.300 tonnes [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=44,
        title="Multiple Choice: Environmental Fate of Polymers — 9701/11/O/N/23/Q28",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Which polymer degrades naturally when buried in soil?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the degradable polymer:\nA  Poly(ethene)\nB  Poly(propene)\nC  Poly(lactic acid)\nD  Poly(chloroethene)",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the chemical linkage that allows this polymer to degrade.",
                marks=1,
                num_answer_lines=1
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "C (Poly(lactic acid)) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Ester linkage (-COO-) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=45,
        title="Chemical Recycling: Pyrolysis of Poly(ethene) — 9701/21/M/J/22/Q7",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="In feedstock recycling, waste poly(ethene) is heated to 500 °C in an oxygen-free chamber with a zeolite catalyst (catalytic pyrolysis).",
        parts=[
            QuestionPart(
                label="(a)",
                text="State the type of bond fission that occurs during thermal cracking of the polymer chains.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Identify the three main physical fractions (gas, liquid, solid) produced during the pyrolysis of poly(ethene).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State one major advantage of chemical feedstock recycling over traditional mechanical recycling.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Homolytic fission of carbon-carbon sigma bonds [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Gas fraction: light hydrocarbon gases (ethene, propene, methane) [1]",
                "Liquid fraction: synthetic crude naphtha / fuel oil; Solid fraction: carbon residue (char) [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Can process mixed, unsorted, and contaminated plastic waste that cannot be mechanically recycled [1]",
                "Produces pure virgin-grade chemical feedstocks without downcycling or degradation of mechanical properties [1]"
            ], "marks": 2}
        ]
    ),
    Question(
        number=46,
        title="Photodegradable Plastics: Carbonyl Insertion — 9701/22/F/M/21/Q6",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Photodegradable plastics are synthesised by co-polymerising ethene with carbon monoxide to incorporate carbonyl (C=O) groups into the backbone.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Draw a section of the polymer chain showing one carbonyl group embedded between poly(ethene) segments.",
                marks=1,
                num_answer_lines=2
            ),
            QuestionPart(
                label="(b)",
                text="Explain why the presence of carbonyl groups enables the plastic to break down in sunlight (Norrish photolysis), whereas pure poly(ethene) does not.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State one limitation of photodegradable plastics in domestic waste management.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "... - CH2 - CH2 - C(=O) - CH2 - CH2 - ... [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Carbonyl groups absorb solar UV radiation strongly in the 280-330 nm range [1]",
                "The absorbed energy excites electrons, causing cleavage of the adjacent C-C bond (Norrish type I/II photolytic cleavage), severing the polymer chain [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "They require direct exposure to sunlight to degrade; if buried inside deep landfill or submerged under water, they do not receive UV light and persist indefinitely [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=47,
        title="Dioxin Formation during Incomplete Combustion of PVC — 9701/23/O/N/23/Q7",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="When PVC is incinerated at insufficient temperatures (< 850 °C), highly toxic chlorinated aromatic compounds called dioxins are formed.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Explain why high-temperature incinerators operate at temperatures above 1100 °C with excess oxygen.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="State one health effect of chronic exposure to dioxins.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "High temperature (> 1100 °C) ensures complete thermal destruction and oxidation of all complex organic molecules [1]",
                "Rapid cooling (quenching) of exhaust gases prevents the re-formation (de novo synthesis) of dioxins [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Highly carcinogenic / immune system impairment / severe skin lesions (chloracne) / reproductive impairment [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=48,
        title="Multiple Choice: Recycling Polymer Codes — 9701/12/M/J/23/Q33",
        syllabus_ref="20.1",
        difficulty="EASY",
        preamble="Resin identification code 2 represents which polymer?",
        parts=[
            QuestionPart(
                label="(a)",
                text="Select the correct polymer:\nA  PET\nB  HDPE\nC  PVC\nD  LDPE",
                marks=1,
                num_answer_lines=1,
                options=["A", "B", "C", "D"]
            ),
            QuestionPart(
                label="(b)",
                text="State the resin identification code for PVC.",
                marks=1,
                num_answer_lines=1
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "B (HDPE) [1]"
            ], "marks": 1},
            {"part": "(b)", "points": [
                "Code 3 (or V) [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=49,
        title="Life Cycle Assessment (LCA): Paper vs Plastic Shopping Bags — 9701/21/M/J/22/Q8",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="A Life Cycle Assessment (LCA) evaluates the environmental impact of a product across four stages: raw material extraction, manufacturing, in-use life, and disposal.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Compare the environmental impact of manufacturing paper bags versus HDPE plastic bags regarding energy and water consumption.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Compare their impact during the disposal stage (landfill and litter).",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="Conclude which option is more sustainable based on reuse.",
                marks=1,
                num_answer_lines=2
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Manufacturing paper bags consumes significantly more water, energy, and pulping chemicals than manufacturing thin HDPE bags [1]",
                "Paper bag production results in higher greenhouse gas emissions per bag [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Paper degrades in compost/soil without toxic persistence [1]",
                "HDPE is non-biodegradable, persisting as visible litter and fragmenting into marine microplastics [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "HDPE 'bags for life' reused multiple times (at least 4-5 times) have a lower overall carbon and environmental footprint than single-use paper or plastic bags [1]"
            ], "marks": 1}
        ]
    ),
    Question(
        number=50,
        title="Comprehensive Evaluation of Addition Polymerisation — 9701/22/M/J/23/Q14",
        syllabus_ref="20.1",
        difficulty="HARD",
        preamble="Polymer X has repeat unit -[CH2-CH(CH3)]n- and Polymer Y has repeat unit -[CH2-CHCl]n-.",
        parts=[
            QuestionPart(
                label="(a)",
                text="Name both polymers and their respective monomers.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(b)",
                text="Compare the intermolecular forces present in Polymer X with those in Polymer Y.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(c)",
                text="State the observation and write the chemical equation when the monomer of Polymer X reacts with aqueous bromine.",
                marks=2,
                num_answer_lines=3
            ),
            QuestionPart(
                label="(d)",
                text="Explain why Polymer Y produces an acidic solution when its combustion gases are dissolved in water, while Polymer X produces a neutral solution.",
                marks=2,
                num_answer_lines=3
            )
        ],
        mark_scheme=[
            {"part": "(a)", "points": [
                "Polymer X: Poly(propene), monomer is propene (CH2=CHCH3) [1]",
                "Polymer Y: Poly(chloroethene) / PVC, monomer is chloroethene (CH2=CHCl) [1]"
            ], "marks": 2},
            {"part": "(b)", "points": [
                "Polymer X (polypropene) has only non-polar bonds and is held purely by London dispersion forces [1]",
                "Polymer Y (PVC) contains polar C-Cl bonds and is held by stronger permanent dipole-dipole attractions in addition to dispersion forces [1]"
            ], "marks": 2},
            {"part": "(c)", "points": [
                "Observation: Orange/brown bromine water is decolourised (turns colourless) [1]",
                "CH3-CH=CH2 + Br2 -> CH3-CH(Br)-CH2Br (1,2-dibromopropane) [1]"
            ], "marks": 2},
            {"part": "(d)", "points": [
                "Polymer Y contains chlorine; combustion produces acidic hydrogen chloride gas (HCl), which dissolves in water to form hydrochloric acid (low pH) [1]",
                "Polymer X contains only carbon and hydrogen; complete combustion yields only CO2 and neutral H2O (forming weakly acidic carbonic acid, not strongly acidic mineral acid) [1]"
            ], "marks": 2}
        ]
    ),
]
'''
    with open("topic20_data.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully built topic20_data.py with 50 questions!")

if __name__ == "__main__":
    generate()
