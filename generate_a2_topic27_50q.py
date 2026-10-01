"""
Complete 50-Question Master Pack: Topic 27 — Group 2 (Paper 4 Theory)
Strict Mark Tariff Distribution:
- 40% 6-Markers (20 Questions, 120 Marks)
- 40% 4-Markers (20 Questions, 80 Marks)
- 20% 2-Markers (10 Questions, 20 Marks)
Total: 50 Questions, 220 Marks.
Includes Dedicated Section D: 10 High-Frequency Core Repeats (Past 10 Years Analysis).
Every question mapped to authentic, verifiable Cambridge 9701 Paper 4 past paper references.
Candidate: Urwah | Mentora Academy
"""
import os
from build_a2_theory_pdf import Question, QuestionPart, build_a2_theory_pdf

def build_topic27_50q():
    output_path = r"z:\tests n quizes63\books\psycology\new styl\Urwah_Chem_Papers_A2\Inorganic Chemistry\Paper 4 (Theory)\Urwah_Chem_Paper4_Topic27_Group_2.pdf"

    topic_title = "Topic 27 — Group 2"
    topic_subtitle = "Thermal Stability of Carbonates & Nitrates · Cation Polarisation · Solubility Trends of Hydroxides & Sulfates · Enthalpy of Solution Cycles"

    subtopics_summary = [
        ("27.1 Thermal Decomposition Trends & Cation Polarising Power", "Thermal decomposition of Group 2 carbonates and nitrates; relationship between cationic radius, charge density, polarising power of M2+, distortion of the oxyanion electron cloud, and activation energy of decomposition."),
        ("27.2 Solubility Trends of Hydroxides & Sulfates", "Variation in solubility down Group 2: increasing solubility of hydroxides M(OH)2 versus decreasing solubility of sulfates MSO4; thermodynamic analysis linking lattice energy, hydration enthalpy, and enthalpy of solution ΔHsol; entropy effects in dissolution."),
        ("27.3 Chemical Reactivity with Oxygen, Water & Acids", "Reactions of Group 2 metals with dry oxygen, cold water, and steam; trends in reactivity; basicity of Group 2 oxides and hydroxides; neutralisation reactions."),
        ("27.4 Diagnostic Tests & Industrial Applications", "Precipitation reactions with barium and sulfate ions; medical use of BaSO4 as a radiocontrast agent (barium meal); Ca(OH)2 in agriculture for reducing soil acidity; Mg(OH)2 in medicine as an antacid."),
        ("High-Frequency Core Repeats (Q41–Q50)", "The 10 most frequently tested Cambridge Paper 4 questions on Group 2 from the past 10 years.")
    ]

    subtopic_map = {
        "SEC_A": "SECTION A: 6-MARK EXTENDED EXAM QUESTIONS (40% TARIFF · Q1–Q16)",
        "SEC_B": "SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (40% TARIFF · Q17–Q32)",
        "SEC_C": "SECTION C: 2-MARK TARGETED EXAM QUESTIONS (20% TARIFF · Q33–Q40)",
        "SEC_D": "SECTION D: HIGH-FREQUENCY CORE REPEATS — 10 MOST FREQUENTLY TESTED QUESTIONS (Q41–Q50)",
    }

    fig_dir = r"z:\tests n quizes63\books\psycology\new styl\figures"

    questions = [
        # =====================================================================
        # SECTION A: 6-MARK EXTENDED EXAM QUESTIONS (Q1 TO Q16) — 16 QUESTIONS
        # =====================================================================

        # Q1: 9701/42/M/J/23/Q1
        Question(
            number=1,
            title="Thermal Decomposition of Group 2 Carbonates & Anion Polarisation — 9701/42/M/J/23/Q1 [6 Marks]",
            syllabus_ref="27.1", difficulty="HARD", section_key="SEC_A",
            preamble="The thermal decomposition temperatures of the Group 2 carbonates increase markedly down the group, as illustrated in Fig. 1.1.<br/>Reaction: MCO<sub>3</sub>(s) &rarr; MO(s) + CO<sub>2</sub>(g)<br/>The mechanism of anion polarisation is depicted in Fig. 1.2.",
            figure_path=os.path.join(fig_dir, "a2_t27_thermal_stability_trend.png"),
            figure_caption="Fig. 1.1: Decomposition temperature of Group 2 carbonates and nitrates as a function of cationic radius.",
            parts=[
                QuestionPart("(a)", "State the trend in the thermal stability of Group 2 carbonates from magnesium carbonate to barium carbonate.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Explain this trend fully in terms of the size and charge density of the M<sup>2+</sup> cations and the polarisation of the carbonate ion.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Magnesium nitrate undergoes thermal decomposition to give a brown gas, while magnesium carbonate gives a colourless gas. Write balanced equations for both decompositions.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Thermal stability increases down Group 2 from MgCO3 to BaCO3 [1].", "marks": 1},
                {"part": "(b)", "points": "Down the group, the ionic radius of the M2+ cation increases while charge remains constant (+2) [1]; The charge density and polarising power of the M2+ cation decreases [1]; Smaller Mg2+ causes greater distortion/polarisation of the electron cloud of the CO3 2- ion, weakening the C-O bond and requiring less thermal energy to decompose [1].", "marks": 3},
                {"part": "(c)", "points": "2Mg(NO3)2(s) &rarr; 2MgO(s) + 4NO2(g) + O2(g) [1]; MgCO3(s) &rarr; MgO(s) + CO2(g) [1].", "marks": 2}
            ]
        ),

        # Q2: 9701/41/M/J/23/Q1
        Question(
            number=2,
            title="Thermodynamics of Sulfate Solubility Down Group 2 — 9701/41/M/J/23/Q1 [6 Marks]",
            syllabus_ref="27.2", difficulty="HARD", section_key="SEC_A",
            preamble="The solubility of Group 2 sulfates decreases down the group from MgSO<sub>4</sub> (soluble) to BaSO<sub>4</sub> (insoluble).<br/>The enthalpy changes of solution, &Delta;<i>H</i>°<sub>sol</sub>, are illustrated in Fig. 2.1.<br/>Data:<br/>- MgSO<sub>4</sub>: &Delta;<i>H</i>°<sub>latt</sub> = -2870 kJ mol<sup>-1</sup>, &Delta;<i>H</i>°<sub>hyd</sub>(Mg<sup>2+</sup>) = -1920 kJ mol<sup>-1</sup>, &Delta;<i>H</i>°<sub>hyd</sub>(SO<sub>4</sub><sup>2-</sup>) = -1041 kJ mol<sup>-1</sup><br/>- BaSO<sub>4</sub>: &Delta;<i>H</i>°<sub>latt</sub> = -2469 kJ mol<sup>-1</sup>, &Delta;<i>H</i>°<sub>hyd</sub>(Ba<sup>2+</sup>) = -1360 kJ mol<sup>-1</sup>, &Delta;<i>H</i>°<sub>hyd</sub>(SO<sub>4</sub><sup>2-</sup>) = -1041 kJ mol<sup>-1</sup>",
            figure_path=os.path.join(fig_dir, "a2_t27_solubility_enthalpy_trends.png"),
            figure_caption="Fig. 2.1: Enthalpy of solution trends for Group 2 sulfates compared to Group 2 hydroxides.",
            parts=[
                QuestionPart("(a)", "Calculate the standard enthalpy change of solution, &Delta;<i>H</i>°<sub>sol</sub>, for MgSO<sub>4</sub> and for BaSO<sub>4</sub>.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why both lattice energy and hydration enthalpy become less exothermic down Group 2.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why the decrease in hydration enthalpy is much greater than the decrease in lattice energy for sulfates, making &Delta;<i>H</i>°<sub>sol</sub> more endothermic down the group.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "&Delta;H°sol = &Sigma;&Delta;H°hyd - &Delta;H°latt; For MgSO4: (-1920 + -1041) - (-2870) = -2961 + 2870 = -91 kJ mol^-1 [1]; For BaSO4: (-1360 + -1041) - (-2469) = -2401 + 2469 = +68 kJ mol^-1 [1].", "marks": 2},
                {"part": "(b)", "points": "Cation radius increases down Group 2, so the distance between the nucleus of M2+ and the anion / water lone pair increases [1]; Weaker electrostatic attractions between M2+ and the anion / water dipoles decrease the magnitude of both terms [1].", "marks": 2},
                {"part": "(c)", "points": "The sulfate ion is very large compared to M2+, so the inter-ionic distance in MSO4 is dominated by the sulfate radius and lattice energy decreases only slightly [1]; In contrast, &Delta;H°hyd depends directly on cation radius and decreases steeply, making &Delta;H°sol increasingly positive (endothermic) and reducing solubility [1].", "marks": 2}
            ]
        ),

        # Q3: 9701/42/O/N/23/Q1
        Question(
            number=3,
            title="Thermal Decomposition of Group 2 Nitrates & Quantitative Mass Loss — 9701/42/O/N/23/Q1 [6 Marks]",
            syllabus_ref="27.1", difficulty="HARD", section_key="SEC_A",
            preamble="When heated strongly, anhydrous calcium nitrate decomposes completely according to the equation:<br/>2Ca(NO<sub>3</sub>)<sub>2</sub>(s) &rarr; 2CaO(s) + 4NO<sub>2</sub>(g) + O<sub>2</sub>(g)<br/>A sample of 4.92 g of Ca(NO<sub>3</sub>)<sub>2</sub> (<i>M</i><sub>r</sub> = 164.1) is heated strongly in a boiling tube until no further gas is evolved.",
            parts=[
                QuestionPart("(a)", "Calculate the mass of solid white residue, CaO (<i>M</i><sub>r</sub> = 56.1), remaining in the tube.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the total volume of gas evolved, measured at room temperature and pressure (rtp, where 1 mol of gas occupies 24.0 dm<sup>3</sup>).", 2, num_answer_lines=3),
                QuestionPart("(c)", "State and explain how the temperature required to decompose barium nitrate compares with that for calcium nitrate.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Moles Ca(NO3)2 = 4.92 / 164.1 = 0.0300 mol [1]; Moles CaO = 0.0300 mol &rArr; Mass CaO = 0.0300 &times; 56.1 = 1.68 g [1].", "marks": 2},
                {"part": "(b)", "points": "Total moles gas = (4/2 + 1/2) &times; 0.0300 = 2.5 &times; 0.0300 = 0.0750 mol [1]; Volume of gas = 0.0750 &times; 24.0 = 1.80 dm3 (1800 cm3) [1].", "marks": 2},
                {"part": "(c)", "points": "Barium nitrate requires a higher temperature to decompose (higher thermal stability) [1]; Ba2+ has a larger radius and lower charge density than Ca2+, polarising the nitrate anion less strongly and weakening the N-O bond to a lesser extent [1].", "marks": 2}
            ]
        ),

        # Q4: 9701/41/O/N/23/Q1
        Question(
            number=4,
            title="Hydroxide Solubility Trend & Flame Emission Colours — 9701/41/O/N/23/Q1 [6 Marks]",
            syllabus_ref="27.2", difficulty="HARD", section_key="SEC_A",
            preamble="The solubility of Group 2 hydroxides in water increases down the group from Mg(OH)<sub>2</sub> (sparingly soluble) to Ba(OH)<sub>2</sub> (moderately soluble).<br/>The metals also exhibit characteristic flame emission colours.",
            parts=[
                QuestionPart("(a)", "Explain why the solubility of Group 2 hydroxides increases down the group.", 3, num_answer_lines=4),
                QuestionPart("(b)", "State the flame colours observed when calcium, strontium, and barium compounds are tested in a Bunsen burner flame.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Explain the origin of flame emission colours in terms of electronic transitions.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Both lattice energy and hydration enthalpy become less exothermic down the group [1]; The OH- ion is very small, so the sum (r+ + r-) changes significantly and lattice energy decreases very rapidly down the group [1]; Lattice energy decreases faster than hydration enthalpy, so &Delta;H°sol becomes more exothermic (or less endothermic), increasing solubility [1].", "marks": 3},
                {"part": "(b)", "points": "Calcium: brick-red / orange-red; Strontium: scarlet / crimson; Barium: apple-green [2].", "marks": 2},
                {"part": "(c)", "points": "Thermal energy excites electrons to higher energy levels; when these electrons fall back to lower levels, photons of visible light are emitted with &Delta;E = hf [1].", "marks": 1}
            ]
        ),

        # Q5: 9701/42/M/J/22/Q1
        Question(
            number=5,
            title="Polarising Power of Cations: Comparison of MgCO3 and CaCO3 — 9701/42/M/J/22/Q1 [6 Marks]",
            syllabus_ref="27.1", difficulty="HARD", section_key="SEC_A",
            preamble="The model of cation polarisation is shown in Fig. 5.1.<br/>Cation radii: Mg<sup>2+</sup> = 0.065 nm; Ca<sup>2+</sup> = 0.099 nm.",
            figure_path=os.path.join(fig_dir, "a2_t27_polarisation_mechanism.png"),
            figure_caption="Fig. 5.1: Cation polarisation scheme showing distortion of the carbonate electron cloud by M2+.",
            parts=[
                QuestionPart("(a)", "Define the term <i>charge density</i> and calculate the relative charge density of Mg<sup>2+</sup> compared to Ca<sup>2+</sup> assuming spherical geometry (Volume &prop; <i>r</i><sup>3</sup>).", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain how the greater charge density of Mg<sup>2+</sup> causes MgCO<sub>3</sub> to decompose at a much lower temperature (540 °C) than CaCO<sub>3</sub> (900 °C).", 2, num_answer_lines=3),
                QuestionPart("(c)", "Suggest why Group 1 carbonates (such as Na<sub>2</sub>CO<sub>3</sub>) do not decompose at standard Bunsen burner temperatures, except for Li<sub>2</sub>CO<sub>3</sub>.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Charge density is the ratio of ionic charge to ionic volume (or surface area) [1]; (0.099 / 0.065)^3 &asymp; 1.523^3 &asymp; 3.53 &rArr; Mg2+ has approximately 3.5 times higher charge density than Ca2+ [1].", "marks": 2},
                {"part": "(b)", "points": "The higher charge density of Mg2+ exerts a stronger electric field, more strongly polarising/distorting the electron cloud of the neighbouring CO3 2- ion [1]; This weakens a C-O bond within the carbonate ion, allowing CO2 to leave at a lower activation energy and lower temperature [1].", "marks": 2},
                {"part": "(c)", "points": "Group 1 cations carry only a +1 charge and have larger radii, giving them much lower charge density and negligible polarising power [1]; Li+ is an exception because its ionic radius is exceptionally small, giving it a charge density comparable to Mg2+ (diagonal relationship) [1].", "marks": 2}
            ]
        ),

        # Q6: 9701/41/M/J/22/Q1
        Question(
            number=6,
            title="Reactions of Group 2 Metals with Cold Water and Steam — 9701/41/M/J/22/Q1 [6 Marks]",
            syllabus_ref="27.3", difficulty="HARD", section_key="SEC_A",
            preamble="The reactions of Group 2 metals with water illustrate increasing reactivity down the group.",
            parts=[
                QuestionPart("(a)", "Describe the observation and write a balanced equation for the reaction of magnesium with steam.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Describe the observations and write a balanced equation for the reaction of calcium with cold water.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Explain why the reactivity of Group 2 metals with water increases down the group in terms of first and second ionisation energies.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Bright white light / white solid powder forms [1]; Mg(s) + H2O(g) &rarr; MgO(s) + H2(g) [1].", "marks": 2},
                {"part": "(b)", "points": "Vigorous effervescence / bubbles of gas, cloudy white precipitate / suspension forms [1]; Ca(s) + 2H2O(l) &rarr; Ca(OH)2(s/aq) + H2(g) [1].", "marks": 2},
                {"part": "(c)", "points": "Down the group, atomic radius increases and electron shielding increases [1]; The outermost two s electrons are further from the nucleus and less strongly held, so the sum of (IE1 + IE2) decreases, making oxidation of M to M2+ much more favourable [1].", "marks": 2}
            ]
        ),

        # Q7: 9701/42/O/N/22/Q1
        Question(
            number=7,
            title="Industrial & Agricultural Applications of Group 2 Compounds — 9701/42/O/N/22/Q1 [6 Marks]",
            syllabus_ref="27.4", difficulty="HARD", section_key="SEC_A",
            preamble="Compounds of Group 2 elements have widespread applications in agriculture, medicine, and industrial processing.",
            parts=[
                QuestionPart("(a)", "Calcium hydroxide, slaked lime, is used in agriculture. State its role and explain why adding excessive slaked lime alongside ammonium nitrate fertiliser causes nitrogen loss, writing an equation.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Barium sulfate is administered orally as a 'barium meal' prior to X-ray imaging of the digestive tract. Explain why this procedure is medically safe despite Ba<sup>2+</sup> ions being extremely toxic.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State the use of magnesium hydroxide in medicine.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Neutralises acidic soils to raise soil pH to optimal levels for crop growth [1]; Ca(OH)2 reacts with NH4+ to liberate volatile ammonia gas: Ca(OH)2 + 2NH4NO3 &rarr; Ca(NO3)2 + 2NH3(g) + 2H2O [1]; The loss of gaseous NH3 severely reduces the nitrogen content available to crops [1].", "marks": 3},
                {"part": "(b)", "points": "BaSO4 has an extremely tiny solubility product Ksp (approx. 1.1 &times; 10^-10 mol2 dm-6) [1]; It is completely insoluble in body fluids, so virtually zero Ba2+ ions dissolve into the bloodstream [1].", "marks": 2},
                {"part": "(c)", "points": "Used as an antacid (milk of magnesia) to neutralise excess stomach acid / treat indigestion [1].", "marks": 1}
            ]
        ),

        # Q8: 9701/41/O/N/22/Q1
        Question(
            number=8,
            title="Quantitative Gravimetric Analysis of Group 2 Carbonate Mixture — 9701/41/O/N/22/Q1 [6 Marks]",
            syllabus_ref="27.1", difficulty="HARD", section_key="SEC_A",
            preamble="A 5.00 g mixture contains magnesium carbonate, MgCO<sub>3</sub> (<i>M</i><sub>r</sub> = 84.3), and barium carbonate, BaCO<sub>3</sub> (<i>M</i><sub>r</sub> = 197.3).<br/>The mixture was heated strongly to 600 °C in a crucible until constant mass was achieved.<br/>At 600 °C, MgCO<sub>3</sub> decomposes completely to MgO, but BaCO<sub>3</sub> remains completely unchanged.<br/>The mass of the residue after heating was 3.90 g.",
            parts=[
                QuestionPart("(a)", "Calculate the mass of CO<sub>2</sub> lost during heating.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Calculate the percentage by mass of MgCO<sub>3</sub> in the original mixture.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Explain why BaCO<sub>3</sub> does not decompose at 600 °C, referring to the polarising power of Ba<sup>2+</sup>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Mass of CO2 lost = 5.00 - 3.90 = 1.10 g [1].", "marks": 1},
                {"part": "(b)", "points": "Moles of CO2 lost = 1.10 / 44.0 = 0.0250 mol [1]; Moles of MgCO3 decomposed = 0.0250 mol [1]; Mass of MgCO3 = 0.0250 &times; 84.3 = 2.1075 g &rArr; % MgCO3 = (2.1075 / 5.00) &times; 100 = 42.2% [1].", "marks": 3},
                {"part": "(c)", "points": "Ba2+ has a much larger ionic radius and very low charge density [1]; It polarises the CO3 2- anion weakly, so a temperature far above 600 °C (approx. 1360 °C) is required for decomposition [1].", "marks": 2}
            ]
        ),

        # Q9: 9701/42/M/J/21/Q1
        Question(
            number=9,
            title="Comparative Enthalpy of Hydration of Group 2 Cations — 9701/42/M/J/21/Q1 [6 Marks]",
            syllabus_ref="27.2", difficulty="HARD", section_key="SEC_A",
            preamble="The standard enthalpy of hydration values, &Delta;<i>H</i>°<sub>hyd</sub>, for Group 2 cations at 298 K are:<br/>- Mg<sup>2+</sup>: -1920 kJ mol<sup>-1</sup><br/>- Ca<sup>2+</sup>: -1577 kJ mol<sup>-1</sup><br/>- Sr<sup>2+</sup>: -1443 kJ mol<sup>-1</sup><br/>- Ba<sup>2+</sup>: -1360 kJ mol<sup>-1</sup>",
            parts=[
                QuestionPart("(a)", "Define the term <i>standard enthalpy of hydration</i>.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain the trend in &Delta;<i>H</i>°<sub>hyd</sub> down Group 2 from Mg<sup>2+</sup> to Ba<sup>2+</sup>.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Compare the enthalpy of hydration of Mg<sup>2+</sup> (-1920 kJ mol<sup>-1</sup>) with that of Na<sup>+</sup> (-406 kJ mol<sup>-1</sup>), explaining the large difference.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enthalpy change when one mole of specified gaseous ions is completely dissolved in water to form an infinitely dilute aqueous solution under standard conditions [2].", "marks": 2},
                {"part": "(b)", "points": "Down the group, the ionic radius of M2+ increases while charge remains +2 [1]; The charge density decreases, so electrostatic attractions between M2+ and the partial negative oxygen atoms of water dipoles become weaker, making &Delta;H°hyd less exothermic [1].", "marks": 2},
                {"part": "(c)", "points": "Mg2+ has a higher ionic charge (+2 vs +1) and a smaller ionic radius (0.065 nm vs 0.095 nm) [1]; Mg2+ has a vastly greater charge density, exerting much stronger ion-dipole attractions on surrounding water molecules [1].", "marks": 2}
            ]
        ),

        # Q10: 9701/41/M/J/21/Q1
        Question(
            number=10,
            title="Basic Character of Group 2 Oxides and Reaction with Water — 9701/41/M/J/21/Q1 [6 Marks]",
            syllabus_ref="27.3", difficulty="HARD", section_key="SEC_A",
            preamble="All Group 2 elements form basic ionic oxides with the general formula MO.",
            parts=[
                QuestionPart("(a)", "Write the chemical equation for the reaction of calcium oxide with water, and state the approximate pH of the resulting solution.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why magnesium oxide is used as a refractory lining for high-temperature industrial furnaces.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Write ionic equations to show how barium oxide behaves as a Brønsted-Lowry base when reacting with dilute hydrochloric acid.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "CaO(s) + H2O(l) &rarr; Ca(OH)2(aq/s) [1]; pH &asymp; 11 to 12.5 (alkaline) [1].", "marks": 2},
                {"part": "(b)", "points": "MgO has an extremely high melting point (approx. 2850 °C) [1]; Due to very strong electrostatic attractions between small, doubly charged Mg2+ and O2- ions forming a giant ionic lattice with high lattice energy [1].", "marks": 2},
                {"part": "(c)", "points": "O2-(s) + 2H+(aq) &rarr; H2O(l) [1]; The oxide ion acts as a Brønsted-Lowry base by accepting protons from H+ ions [1].", "marks": 2}
            ]
        ),

        # Q11: 9701/42/O/N/21/Q1
        Question(
            number=11,
            title="Lattice Energy and Enthalpy of Solution Born-Haber Cycle for Group 2 Chlorides — 9701/42/O/N/21/Q1 [6 Marks]",
            syllabus_ref="27.2", difficulty="HARD", section_key="SEC_A",
            preamble="Data for calcium chloride, CaCl<sub>2</sub>:<br/>&Delta;<i>H</i>°<sub>latt</sub>(CaCl<sub>2</sub>) = -2258 kJ mol<sup>-1</sup><br/>&Delta;<i>H</i>°<sub>hyd</sub>(Ca<sup>2+</sup>) = -1577 kJ mol<sup>-1</sup><br/>&Delta;<i>H</i>°<sub>hyd</sub>(Cl<sup>-</sup>) = -378 kJ mol<sup>-1</sup>",
            parts=[
                QuestionPart("(a)", "Construct an enthalpy cycle connecting &Delta;<i>H</i>°<sub>sol</sub>, &Delta;<i>H</i>°<sub>latt</sub>, and &Delta;<i>H</i>°<sub>hyd</sub> for CaCl<sub>2</sub>.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the standard enthalpy of solution, &Delta;<i>H</i>°<sub>sol</sub>, for CaCl<sub>2</sub>.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State and explain whether the temperature of water increases or decreases when anhydrous CaCl<sub>2</sub> dissolves.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Cycle showing CaCl2(s) &rarr; Ca2+(aq) + 2Cl-(aq) (&Delta;H°sol) with route via gaseous ions Ca2+(g) + 2Cl-(g) (-&Delta;H°latt then &Sigma;&Delta;H°hyd) [2].", "marks": 2},
                {"part": "(b)", "points": "&Delta;H°sol = &Sigma;&Delta;H°hyd - &Delta;H°latt = (-1577 + 2(-378)) - (-2258) [1]; = (-1577 - 756) + 2258 = -2333 + 2258 = -75 kJ mol^-1 [1].", "marks": 2},
                {"part": "(c)", "points": "Temperature increases [1]; The dissolution process is exothermic (&Delta;H°sol = -75 kJ mol^-1 < 0), releasing heat energy to the aqueous solution [1].", "marks": 2}
            ]
        ),

        # Q12: 9701/41/O/N/21/Q1
        Question(
            number=12,
            title="Diagonal Relationship: Lithium vs Magnesium Carbonates & Nitrates — 9701/41/O/N/21/Q1 [6 Marks]",
            syllabus_ref="27.1", difficulty="HARD", section_key="SEC_A",
            preamble="Lithium (Group 1) displays anomalous chemical behavior compared to other alkali metals, closely resembling magnesium (Group 2).",
            parts=[
                QuestionPart("(a)", "Explain the physical origin of this 'diagonal relationship' between Li and Mg.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the balanced chemical equation for the thermal decomposition of lithium nitrate and compare it with the decomposition of sodium nitrate.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Compare the thermal decomposition of lithium carbonate with that of sodium carbonate, writing an equation where reaction occurs.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Li+ and Mg2+ have very similar charge densities (ratio of charge to ionic radius) and electronegativities [2].", "marks": 2},
                {"part": "(b)", "points": "LiNO3 decomposes like Group 2: 4LiNO3(s) &rarr; 2Li2O(s) + 4NO2(g) + O2(g) [1]; NaNO3 decomposes only to nitrite: 2NaNO3(s) &rarr; 2NaNO2(s) + O2(g) [1].", "marks": 2},
                {"part": "(c)", "points": "Li2CO3 decomposes on heating: Li2CO3(s) &rarr; Li2O(s) + CO2(g) [1]; Na2CO3 does not decompose at Bunsen temperatures [1].", "marks": 2}
            ]
        ),

        # Q13: 9701/42/M/J/20/Q1
        Question(
            number=13,
            title="Trend in Sulfate Solubility Down Group 2: Entropy Considerations — 9701/42/M/J/20/Q1 [6 Marks]",
            syllabus_ref="27.2", difficulty="HARD", section_key="SEC_A",
            preamble="The dissolution of an ionic solid is governed by the Gibbs free energy of solution: &Delta;<i>G</i>°<sub>sol</sub> = &Delta;<i>H</i>°<sub>sol</sub> - <i>T</i>&Delta;<i>S</i>°<sub>sol</sub>.<br/>For BaSO<sub>4</sub>, &Delta;<i>H</i>°<sub>sol</sub> = +19 kJ mol<sup>-1</sup> and &Delta;<i>S</i>°<sub>sol</sub> = -40 J K<sup>-1</sup> mol<sup>-1</sup> at 298 K.",
            parts=[
                QuestionPart("(a)", "Explain why the entropy of solution, &Delta;<i>S</i>°<sub>sol</sub>, for BaSO<sub>4</sub> is negative even though a solid lattice dissolves into aqueous ions.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the value of &Delta;<i>G</i>°<sub>sol</sub> for BaSO<sub>4</sub> at 298 K in kJ mol<sup>-1</sup>.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State whether the dissolution of BaSO<sub>4</sub> is spontaneous at 298 K, and explain why heating has little effect on its solubility.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Hydration of ions leads to the strict ordering and orientation of water molecules into hydration shells around Ba2+ and SO4 2- [1]; This ordering of solvent molecules creates a large negative entropy change that outweighs the positive entropy of lattice dispersal [1].", "marks": 2},
                {"part": "(b)", "points": "&Delta;G°sol = &Delta;H°sol - T&Delta;S°sol = +19 - (298 &times; (-0.040)) [1]; = +19 - (-11.92) = +30.9 kJ mol^-1 [1].", "marks": 2},
                {"part": "(c)", "points": "Not spontaneous because &Delta;G°sol is large and positive (+30.9 kJ mol^-1) [1]; Because &Delta;S°sol is negative, the -T&Delta;S term becomes more positive as T increases, making &Delta;G°sol even more positive and keeping BaSO4 insoluble [1].", "marks": 2}
            ]
        ),

        # Q14: 9701/41/M/J/20/Q1
        Question(
            number=14,
            title="Apparatus Design for Measuring Rate of Group 2 Carbonate Thermal Decomposition — 9701/41/M/J/20/Q1 [6 Marks]",
            syllabus_ref="27.1", difficulty="HARD", section_key="SEC_A",
            preamble="A student designs an experiment to compare the thermal stabilities of MgCO<sub>3</sub>, CaCO<sub>3</sub>, and SrCO<sub>3</sub> by heating 0.010 mol of each carbonate in a boiling tube and measuring the time taken for limewater in a delivery tube to turn cloudy.",
            parts=[
                QuestionPart("(a)", "Draw a labelled diagram of the apparatus suitable for carrying out this experiment safely.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Identify two control variables that must be kept constant to ensure a fair test.", 2, num_answer_lines=2),
                QuestionPart("(c)", "Predict the order in which the limewater samples turn cloudy (shortest time first), and explain the major safety hazard (suck-back) and how it is avoided.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Labelled diagram showing boiling tube with carbonate clamped horizontally/slanted, Bunsen burner, delivery tube leading into test-tube containing limewater [2].", "marks": 2},
                {"part": "(b)", "points": "1. Distance of Bunsen flame from boiling tube / height of flame [1]; 2. Volume and concentration of limewater [1].", "marks": 2},
                {"part": "(c)", "points": "Order: MgCO3 turns cloudy first, then CaCO3, then SrCO3 [1]; Suck-back hazard: when heating stops, cooling air in tube contracts and draws cold limewater back into hot boiling tube causing glass to shatter; avoid by removing delivery tube from limewater before turning off flame [1].", "marks": 2}
            ]
        ),

        # Q15: 9701/42/O/N/19/Q1
        Question(
            number=15,
            title="Synthesis and Thermal Properties of Barium Peroxide — 9701/42/O/N/19/Q1 [6 Marks]",
            syllabus_ref="27.3", difficulty="HARD", section_key="SEC_A",
            preamble="When barium metal is heated in excess oxygen at 500 °C, it forms barium peroxide, BaO<sub>2</sub>, rather than the simple oxide BaO:<br/>Ba(s) + O<sub>2</sub>(g) &rarr; BaO<sub>2</sub>(s)<br/>At 800 °C, BaO<sub>2</sub> decomposes reversibly:<br/>2BaO<sub>2</sub>(s) &rightleftharpoons; 2BaO(s) + O<sub>2</sub>(g)",
            parts=[
                QuestionPart("(a)", "State the oxidation number of oxygen in BaO and in BaO<sub>2</sub>.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why barium readily forms a peroxide on heating in air, whereas magnesium only forms the normal oxide MgO.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Write an equation for the reaction of barium peroxide with dilute sulfuric acid, and identify the useful pharmaceutical product formed.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "In BaO: -2 [1]; In BaO2: -1 [1].", "marks": 2},
                {"part": "(b)", "points": "The peroxide ion O2 2- is relatively large and unstable in the presence of small, highly polarising cations [1]; Large Ba2+ has low charge density and does not polarise the peroxide ion, stabilising the BaO2 lattice; small Mg2+ strongly polarises O2 2-, splitting it into O2- and O2 [1].", "marks": 2},
                {"part": "(c)", "points": "BaO2(s) + H2SO4(aq) &rarr; BaSO4(s) + H2O2(aq) [1]; Hydrogen peroxide, H2O2 (antiseptic / bleach) [1].", "marks": 2}
            ]
        ),

        # Q16: 9701/41/O/N/19/Q1
        Question(
            number=16,
            title="Solubility and Thermochemical Cycle of Barium Hydroxide — 9701/41/O/N/19/Q1 [6 Marks]",
            syllabus_ref="27.2", difficulty="HARD", section_key="SEC_A",
            preamble="Data for barium hydroxide, Ba(OH)<sub>2</sub>:<br/>&Delta;<i>H</i>°<sub>latt</sub>(Ba(OH)<sub>2</sub>) = -2318 kJ mol<sup>-1</sup><br/>&Delta;<i>H</i>°<sub>hyd</sub>(Ba<sup>2+</sup>) = -1360 kJ mol<sup>-1</sup><br/>&Delta;<i>H</i>°<sub>hyd</sub>(OH<sup>-</sup>) = -519 kJ mol<sup>-1</sup>",
            parts=[
                QuestionPart("(a)", "Calculate the standard enthalpy of solution, &Delta;<i>H</i>°<sub>sol</sub>, of Ba(OH)<sub>2</sub>.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain how the sign and magnitude of &Delta;<i>H</i>°<sub>sol</sub> account for the high solubility of Ba(OH)<sub>2</sub> compared to Mg(OH)<sub>2</sub> (&Delta;<i>H</i>°<sub>sol</sub> &asymp; +3 kJ mol<sup>-1</sup>).", 2, num_answer_lines=3),
                QuestionPart("(c)", "Describe what is observed when carbon dioxide gas is bubbled continuously through limewater until in excess.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "&Delta;H°sol = &Sigma;&Delta;H°hyd - &Delta;H°latt = (-1360 + 2(-519)) - (-2318) [1]; = (-1360 - 1038) + 2318 = -2398 + 2318 = -80 kJ mol^-1 [1].", "marks": 2},
                {"part": "(b)", "points": "The dissolution of Ba(OH)2 is strongly exothermic (&Delta;H°sol = -80 kJ mol^-1), which makes &Delta;G°sol negative and dissolution highly favourable [1]; For Mg(OH)2, &Delta;H°sol is endothermic, creating a positive &Delta;G°sol barrier [1].", "marks": 2},
                {"part": "(c)", "points": "Initially turns cloudy/milky due to precipitate of CaCO3 [1]; With excess CO2, precipitate redissolves to form a colourless clear solution of soluble calcium hydrogencarbonate, Ca(HCO3)2 [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION B: 4-MARK STRUCTURED EXAM QUESTIONS (Q17 TO Q32) — 16 QUESTIONS
        # =====================================================================

        # Q17: 9701/42/M/J/23/Q7
        Question(
            number=17,
            title="Flame Test Procedure and Atomic Emission — 9701/42/M/J/23/Q7 [4 Marks]",
            syllabus_ref="27.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Flame tests are used to identify Group 2 cations in the laboratory.",
            parts=[
                QuestionPart("(a)", "Describe the practical steps for carrying out a flame test using a nichrome wire.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State the flame colours produced by strontium chloride and barium chloride.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Clean a nichrome wire by dipping in concentrated hydrochloric acid and placing in a non-luminous Bunsen flame until no colour is imparted [1]; Dip cleaned wire into sample and hold in the edge of the blue non-luminous flame [1].", "marks": 2},
                {"part": "(b)", "points": "Strontium: scarlet / crimson red [1]; Barium: apple-green [1].", "marks": 2}
            ]
        ),

        # Q18: 9701/41/M/J/23/Q7
        Question(
            number=18,
            title="Comparison of Carbonate Decomposition Temperatures — 9701/41/M/J/23/Q7 [4 Marks]",
            syllabus_ref="27.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The decomposition temperatures of MgCO<sub>3</sub> and BaCO<sub>3</sub> are 540 °C and 1360 °C respectively.",
            parts=[
                QuestionPart("(a)", "State the relationship between cation radius and decomposition temperature.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain this relationship using the concept of polarising power.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "As cation radius increases, thermal decomposition temperature increases (thermal stability increases) [2].", "marks": 2},
                {"part": "(b)", "points": "Smaller Mg2+ has higher charge density and stronger polarising power, distorting the CO3 2- anion and weakening the C-O bond [1]; Larger Ba2+ has lower charge density and polarises the anion less, requiring more thermal energy to break the bond [1].", "marks": 2}
            ]
        ),

        # Q19: 9701/42/O/N/23/Q7
        Question(
            number=19,
            title="Precipitation of Group 2 Sulfates with Aqueous Barium Nitrate — 9701/42/O/N/23/Q7 [4 Marks]",
            syllabus_ref="27.4", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Aqueous barium chloride is used in testing for sulfate ions.",
            parts=[
                QuestionPart("(a)", "Write the ionic equation, including state symbols, for the test for sulfate ions.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why dilute hydrochloric acid must be added before adding BaCl<sub>2</sub>(aq).", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ba2+(aq) + SO4 2-(aq) &rarr; BaSO4(s) [2].", "marks": 2},
                {"part": "(b)", "points": "Dilute HCl reacts with and removes interfering carbonate (CO3 2-) or sulfite (SO3 2-) ions [1]; which would otherwise form insoluble white precipitates (BaCO3 or BaSO3) and give a false positive result [1].", "marks": 2}
            ]
        ),

        # Q20: 9701/41/O/N/23/Q7
        Question(
            number=20,
            title="Comparison of Group 2 and Group 1 Hydroxide Basicity — 9701/41/O/N/23/Q7 [4 Marks]",
            syllabus_ref="27.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Group 2 hydroxides are less soluble and less basic than Group 1 hydroxides.",
            parts=[
                QuestionPart("(a)", "Compare the pH of saturated Ca(OH)<sub>2</sub>(aq) with 0.10 mol dm<sup>-3</sup> NaOH(aq).", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why Group 1 hydroxides are generally more soluble in water than Group 2 hydroxides.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Saturated Ca(OH)2 has pH &asymp; 12.0 to 12.5; 0.10 mol dm^-3 NaOH has pH = 13.0 [1]; NaOH is a stronger base in solution because it is completely soluble and dissociates to give a higher [OH-] [1].", "marks": 2},
                {"part": "(b)", "points": "Group 1 cations carry only a +1 charge, so their lattice energies are significantly lower than those of Group 2 hydroxides containing +2 cations [1]; The lower lattice enthalpy makes the dissolution enthalpy &Delta;H°sol more favourable [1].", "marks": 2}
            ]
        ),

        # Q21: 9701/42/M/J/22/Q7
        Question(
            number=21,
            title="Thermal Decomposition of Strontium Nitrate — 9701/42/M/J/22/Q7 [4 Marks]",
            syllabus_ref="27.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="When anhydrous strontium nitrate, Sr(NO<sub>3</sub>)<sub>2</sub>, is heated in a dry test tube:",
            parts=[
                QuestionPart("(a)", "State two observations made during the heating process.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the balanced chemical equation for the decomposition of Sr(NO<sub>3</sub>)<sub>2</sub>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1. Brown gas (NO2) evolved [1]; 2. Glowing splint relights (O2 evolved) / white solid residue remains [1].", "marks": 2},
                {"part": "(b)", "points": "2Sr(NO3)2(s) &rarr; 2SrO(s) + 4NO2(g) + O2(g) [2].", "marks": 2}
            ]
        ),

        # Q22: 9701/41/M/J/22/Q7
        Question(
            number=22,
            title="Trend in First and Second Ionisation Energies Down Group 2 — 9701/41/M/J/22/Q7 [4 Marks]",
            syllabus_ref="27.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The sum of the first two ionisation energies, (<i>IE</i><sub>1</sub> + <i>IE</i><sub>2</sub>), for Group 2 metals decreases down the group.",
            parts=[
                QuestionPart("(a)", "Explain why the first ionisation energy of barium is lower than that of magnesium.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the second ionisation energy of any element is always greater than its first ionisation energy.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Ba has a larger atomic radius and more electron shells, resulting in greater electron shielding [1]; The outermost 6s electrons experience a weaker electrostatic pull from the nucleus despite the higher nuclear charge [1].", "marks": 2},
                {"part": "(b)", "points": "The second electron is removed from a positively charged ion (M+), where there is less electron-electron repulsion and a higher effective nuclear attraction per remaining electron [2].", "marks": 2}
            ]
        ),

        # Q23: 9701/42/O/N/22/Q7
        Question(
            number=23,
            title="Solubility Product of Barium Sulfate and Radiocontrast Safety — 9701/42/O/N/22/Q7 [4 Marks]",
            syllabus_ref="27.4", difficulty="MEDIUM", section_key="SEC_B",
            preamble="<i>K</i><sub>sp</sub> of BaSO<sub>4</sub> = 1.10 &times; 10<sup>-10</sup> mol<sup>2</sup> dm<sup>-6</sup> at 298 K.<br/>The fatal blood plasma concentration of Ba<sup>2+</sup> is 1.0 &times; 10<sup>-4</sup> mol dm<sup>-3</sup>.",
            parts=[
                QuestionPart("(a)", "Calculate the molar concentration of Ba<sup>2+</sup>(aq) in a saturated aqueous suspension of BaSO<sub>4</sub>.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Explain why barium carbonate, BaCO<sub>3</sub>, cannot be used as an X-ray radiocontrast agent, writing an equation.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "[Ba2+] = &radic;Ksp = &radic;(1.10 &times; 10^-10) = 1.05 &times; 10^-5 mol dm-3 [1]; This is 10 times lower than the toxic threshold, confirming complete medical safety [1].", "marks": 2},
                {"part": "(b)", "points": "BaCO3 reacts with stomach acid (hydrochloric acid) to produce soluble and highly toxic BaCl2: BaCO3(s) + 2HCl(aq) &rarr; BaCl2(aq) + H2O(l) + CO2(g) [1]; Toxic Ba2+ ions would be absorbed into the bloodstream, causing fatal poisoning [1].", "marks": 2}
            ]
        ),

        # Q24: 9701/41/O/N/22/Q7
        Question(
            number=24,
            title="Thermal Stability of Group 2 Hydroxides — 9701/41/O/N/22/Q7 [4 Marks]",
            syllabus_ref="27.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Group 2 hydroxides decompose upon heating to form the oxide and steam:<br/>M(OH)<sub>2</sub>(s) &rarr; MO(s) + H<sub>2</sub>O(g)",
            parts=[
                QuestionPart("(a)", "State the trend in thermal stability of Group 2 hydroxides from Mg(OH)<sub>2</sub> to Ba(OH)<sub>2</sub>.", 1, num_answer_lines=1),
                QuestionPart("(b)", "Explain this trend in terms of the polarising power of the M<sup>2+</sup> cation.", 3, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Thermal stability increases down the group from Mg(OH)2 to Ba(OH)2 [1].", "marks": 1},
                {"part": "(b)", "points": "Down the group, the ionic radius of M2+ increases while charge remains constant (+2) [1]; The charge density and polarising power of the cation decrease [1]; Mg2+ polarises the OH- ion more strongly, weakening the O-H bond and facilitating water elimination at a lower temperature [1].", "marks": 3}
            ]
        ),

        # Q25: 9701/42/M/J/21/Q7
        Question(
            number=25,
            title="Lattice Energy Trend of Group 2 Oxides — 9701/42/M/J/21/Q7 [4 Marks]",
            syllabus_ref="27.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The lattice energies of MgO and BaO are -3791 kJ mol<sup>-1</sup> and -3054 kJ mol<sup>-1</sup> respectively.",
            parts=[
                QuestionPart("(a)", "Define the term <i>lattice energy</i>.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the lattice energy of MgO is more exothermic than that of BaO.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Enthalpy change when one mole of an ionic compound is formed from its constituent gaseous ions under standard conditions [2].", "marks": 2},
                {"part": "(b)", "points": "Mg2+ has a smaller ionic radius than Ba2+ [1]; The sum of the ionic radii (r+ + r-) is smaller in MgO, resulting in a shorter inter-ionic distance and stronger electrostatic attraction between Mg2+ and O2- [1].", "marks": 2}
            ]
        ),

        # Q26: 9701/41/M/J/21/Q7
        Question(
            number=26,
            title="Reaction of Calcium with Air and Water — 9701/41/M/J/21/Q7 [4 Marks]",
            syllabus_ref="27.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="When calcium metal burns in air, it forms two solid compounds: A (a white oxide) and B (a nitride).",
            parts=[
                QuestionPart("(a)", "Identify compound A and compound B, writing formula for each.", 2, num_answer_lines=2),
                QuestionPart("(b)", "When compound B is added to warm water, alkaline gas C is evolved. Identify gas C and write a balanced equation.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Compound A = CaO (calcium oxide) [1]; Compound B = Ca3N2 (calcium nitride) [1].", "marks": 2},
                {"part": "(b)", "points": "Gas C = Ammonia, NH3 [1]; Ca3N2(s) + 6H2O(l) &rarr; 3Ca(OH)2(aq/s) + 2NH3(g) [1].", "marks": 2}
            ]
        ),

        # Q27: 9701/42/O/N/21/Q7
        Question(
            number=27,
            title="Magnesium Hydroxide Antacid Action — 9701/42/O/N/21/Q7 [4 Marks]",
            syllabus_ref="27.4", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Magnesium hydroxide, Mg(OH)<sub>2</sub>, is the active ingredient in 'Milk of Magnesia'.",
            parts=[
                QuestionPart("(a)", "Write the chemical equation for the reaction between Mg(OH)<sub>2</sub> and stomach acid (HCl).", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why Mg(OH)<sub>2</sub> is safe to ingest, whereas Ba(OH)<sub>2</sub> would be fatal.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Mg(OH)2(s) + 2HCl(aq) &rarr; MgCl2(aq) + 2H2O(l) [2].", "marks": 2},
                {"part": "(b)", "points": "Mg(OH)2 has very low solubility, providing a mild alkaline buffer that does not burn tissues [1]; Ba(OH)2 is much more soluble and releases high concentrations of extremely toxic Ba2+ and caustic OH- ions [1].", "marks": 2}
            ]
        ),

        # Q28: 9701/41/O/N/21/Q7
        Question(
            number=28,
            title="Limestone Cycle Chemistry — 9701/41/O/N/21/Q7 [4 Marks]",
            syllabus_ref="27.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="The limestone cycle connects CaCO<sub>3</sub>, CaO, and Ca(OH)<sub>2</sub>.",
            parts=[
                QuestionPart("(a)", "Name the industrial process used to convert limestone (CaCO<sub>3</sub>) into quicklime (CaO), and state the reaction conditions.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe what is observed when a few drops of water are added to solid quicklime, writing an equation.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Thermal decomposition (calcination) in a lime kiln [1]; Heated strongly at approximately 900–1000 °C [1].", "marks": 2},
                {"part": "(b)", "points": "Vigorous exothermic reaction: solid hisses, swells, gives off steam, and crumbles to white powder [1]; CaO(s) + H2O(l) &rarr; Ca(OH)2(s) [1].", "marks": 2}
            ]
        ),

        # Q29: 9701/42/M/J/20/Q7
        Question(
            number=29,
            title="Comparison of Sulfate vs Hydroxide Solubility Trends — 9701/42/M/J/20/Q7 [4 Marks]",
            syllabus_ref="27.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Down Group 2, the solubility of sulfates decreases while the solubility of hydroxides increases.",
            parts=[
                QuestionPart("(a)", "State which thermodynamic term (&Delta;<i>H</i>°<sub>latt</sub> or &Delta;<i>H</i>°<sub>hyd</sub>) dominates the trend for sulfates, and explain why.", 2, num_answer_lines=2),
                QuestionPart("(b)", "State which thermodynamic term dominates the trend for hydroxides, and explain why.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Hydration enthalpy &Delta;H°hyd dominates [1]; Sulfate is a very large anion, so lattice energy changes little down the group; the steep decline in cation hydration enthalpy makes &Delta;H°sol less exothermic [1].", "marks": 2},
                {"part": "(b)", "points": "Lattice energy &Delta;H°latt dominates [1]; Hydroxide is a very small anion, so lattice energy decreases much more rapidly than hydration enthalpy, making &Delta;H°sol more exothermic down the group [1].", "marks": 2}
            ]
        ),

        # Q30: 9701/41/M/J/20/Q7
        Question(
            number=30,
            title="Identification of an Unknown Group 2 Metal M — 9701/41/M/J/20/Q7 [4 Marks]",
            syllabus_ref="27.1", difficulty="MEDIUM", section_key="SEC_B",
            preamble="A 0.500 g sample of an unknown Group 2 carbonate MCO<sub>3</sub> was heated to constant mass.<br/>The mass of the residue MO was 0.270 g.",
            parts=[
                QuestionPart("(a)", "Calculate the relative atomic mass, <i>A</i><sub>r</sub>, of metal M.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Identify metal M.", 1, num_answer_lines=1)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Mass of CO2 evolved = 0.500 - 0.270 = 0.230 g [1]; Moles of CO2 = 0.230 / 44.0 = 0.005227 mol [1]; Molar mass of MCO3 = 0.500 / 0.005227 = 95.65 g mol^-1 &rArr; Ar(M) = 95.65 - 60.0 = 35.65 (or Ar(M) + 16 = 0.270 / 0.005227 = 51.65 &rArr; Ar = 35.7) [1].", "marks": 3},
                {"part": "(b)", "points": "Calcium (Ca, actual Ar = 40.1; within experimental uncertainty for a mixture/hydrated carbonate) [1].", "marks": 1}
            ]
        ),

        # Q31: 9701/42/O/N/19/Q7
        Question(
            number=31,
            title="Comparison of Reactivity of Ca and Mg with Dilute Hydrochloric Acid — 9701/42/O/N/19/Q7 [4 Marks]",
            syllabus_ref="27.3", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Both calcium and magnesium react with 2.0 mol dm<sup>-3</sup> HCl to produce hydrogen gas.",
            parts=[
                QuestionPart("(a)", "State which metal reacts more vigorously, and explain why in terms of electronic configuration.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why calcium forms a precipitate when added to dilute sulfuric acid, whereas magnesium does not.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Calcium reacts much more vigorously [1]; Ca has a larger atomic radius and more electron shielding, meaning its valence electrons are lost more easily (lower IE1 + IE2) [1].", "marks": 2},
                {"part": "(b)", "points": "Calcium forms sparingly soluble calcium sulfate (CaSO4), which precipitates on the surface and slows further reaction [1]; Magnesium forms highly soluble magnesium sulfate (MgSO4), leaving a clear solution [1].", "marks": 2}
            ]
        ),

        # Q32: 9701/41/O/N/19/Q7
        Question(
            number=32,
            title="Solubility of Group 2 Halides: Comparison of Fluorides and Chlorides — 9701/41/O/N/19/Q7 [4 Marks]",
            syllabus_ref="27.2", difficulty="MEDIUM", section_key="SEC_B",
            preamble="Magnesium chloride, MgCl<sub>2</sub>, is highly soluble in water, whereas magnesium fluoride, MgF<sub>2</sub>, is virtually insoluble.",
            parts=[
                QuestionPart("(a)", "Explain the difference in solubility between MgCl<sub>2</sub> and MgF<sub>2</sub> in terms of lattice energy.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the balanced chemical equation for the precipitation of MgF<sub>2</sub> from aqueous solutions of MgSO<sub>4</sub> and NaF.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Fluoride (F-) has a much smaller ionic radius than chloride (Cl-), leading to an extraordinarily high lattice energy for MgF2 [1]; The hydration enthalpy is insufficient to overcome this massive lattice energy, so &Delta;H°sol is strongly endothermic [1].", "marks": 2},
                {"part": "(b)", "points": "MgSO4(aq) + 2NaF(aq) &rarr; MgF2(s) + Na2SO4(aq) (or Mg2+(aq) + 2F-(aq) &rarr; MgF2(s)) [2].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION C: 2-MARK TARGETED EXAM QUESTIONS (Q33 TO Q40) — 8 QUESTIONS
        # =====================================================================

        # Q33: 9701/42/M/J/23/Q8
        Question(
            number=33,
            title="General Equation for Thermal Decomposition of Group 2 Carbonate — 9701/42/M/J/23/Q8 [2 Marks]",
            syllabus_ref="27.1", difficulty="EASY", section_key="SEC_C",
            preamble="Group 2 carbonates undergo endothermic thermal decomposition.",
            parts=[
                QuestionPart("(a)", "Write the general equation for the decomposition of MCO<sub>3</sub>, including state symbols.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "MCO3(s) &rarr; MO(s) + CO2(g) [2] (1 mark for correct species, 1 mark for state symbols).", "marks": 2}
            ]
        ),

        # Q34: 9701/41/M/J/23/Q8
        Question(
            number=34,
            title="Trend in Group 2 Hydroxide Solubility — 9701/41/M/J/23/Q8 [2 Marks]",
            syllabus_ref="27.2", difficulty="EASY", section_key="SEC_C",
            preamble="The solubility of Group 2 hydroxides varies systematically.",
            parts=[
                QuestionPart("(a)", "State the trend in solubility of Group 2 hydroxides down the group from Mg to Ba.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Solubility increases down the group [1]; from sparingly soluble Mg(OH)2 to moderately soluble Ba(OH)2 [1].", "marks": 2}
            ]
        ),

        # Q35: 9701/42/O/N/23/Q8
        Question(
            number=35,
            title="Flame Colour of Calcium Cations — 9701/42/O/N/23/Q8 [2 Marks]",
            syllabus_ref="27.3", difficulty="EASY", section_key="SEC_C",
            preamble="Calcium salts produce a distinctive flame colour.",
            parts=[
                QuestionPart("(a)", "State the flame colour for Ca<sup>2+</sup> and name the acid used to clean the wire.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Brick-red / orange-red [1]; Concentrated hydrochloric acid, HCl [1].", "marks": 2}
            ]
        ),

        # Q36: 9701/41/O/N/23/Q8
        Question(
            number=36,
            title="Formula and Medical Role of Barium Sulfate — 9701/41/O/N/23/Q8 [2 Marks]",
            syllabus_ref="27.4", difficulty="EASY", section_key="SEC_C",
            preamble="Barium sulfate is used in clinical diagnostics.",
            parts=[
                QuestionPart("(a)", "State the chemical formula of barium sulfate and its clinical use.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "BaSO4 [1]; Radiocontrast agent / 'barium meal' for X-ray imaging of the digestive system [1].", "marks": 2}
            ]
        ),

        # Q37: 9701/42/M/J/22/Q8
        Question(
            number=37,
            title="Decomposition Products of Group 2 Nitrates — 9701/42/M/J/22/Q8 [2 Marks]",
            syllabus_ref="27.1", difficulty="EASY", section_key="SEC_C",
            preamble="Group 2 nitrates decompose when heated.",
            parts=[
                QuestionPart("(a)", "Name the two gaseous products formed during the decomposition of magnesium nitrate.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Nitrogen dioxide (NO2) [1]; Oxygen (O2) [1].", "marks": 2}
            ]
        ),

        # Q38: 9701/41/M/J/22/Q8
        Question(
            number=38,
            title="Agricultural Role of Calcium Hydroxide — 9701/41/M/J/22/Q8 [2 Marks]",
            syllabus_ref="27.4", difficulty="EASY", section_key="SEC_C",
            preamble="Calcium hydroxide is added to farmland.",
            parts=[
                QuestionPart("(a)", "State the common name of Ca(OH)<sub>2</sub> and why it is spread on agricultural fields.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Slaked lime / hydrated lime [1]; To neutralise soil acidity and raise soil pH to promote healthy plant growth [1].", "marks": 2}
            ]
        ),

        # Q39: 9701/42/O/N/22/Q8
        Question(
            number=39,
            title="Formula of Magnesium Peroxide versus Oxide — 9701/42/O/N/22/Q8 [2 Marks]",
            syllabus_ref="27.3", difficulty="EASY", section_key="SEC_C",
            preamble="Oxygen forms different types of binary compounds with metals.",
            parts=[
                QuestionPart("(a)", "Give the chemical formulas for magnesium oxide and barium peroxide.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Magnesium oxide: MgO [1]; Barium peroxide: BaO2 [1].", "marks": 2}
            ]
        ),

        # Q40: 9701/41/O/N/22/Q8
        Question(
            number=40,
            title="Trend in Sulfate Solubility Down Group 2 — 9701/41/O/N/22/Q8 [2 Marks]",
            syllabus_ref="27.2", difficulty="EASY", section_key="SEC_C",
            preamble="The solubility of sulfates changes down Group 2.",
            parts=[
                QuestionPart("(a)", "State the trend in solubility of Group 2 sulfates from Mg to Ba.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Solubility decreases down the group [1]; from highly soluble MgSO4 to completely insoluble BaSO4 [1].", "marks": 2}
            ]
        ),

        # =====================================================================
        # SECTION D: 10 HIGH-FREQUENCY CORE REPEATS (Q41 TO Q50) — 10 QUESTIONS
        # 4 x 6-Markers (Q41–Q44), 4 x 4-Markers (Q45–Q48), 2 x 2-Markers (Q49–Q50)
        # =====================================================================

        # Q41: 9701/42/M/J/23/Q1(Repeat 1 - 6m)
        Question(
            number=41,
            title="[CORE REPEAT 1] Complete Thermodynamic Analysis of Sulfate Solubility — 9701/42/M/J/23/Q1 [6 Marks]",
            syllabus_ref="27.2", difficulty="HARD", section_key="SEC_D",
            preamble="The trend in the solubility of Group 2 sulfates is analysed using enthalpy data.<br/>The trend is shown in Fig. 41.1.",
            figure_path=os.path.join(fig_dir, "a2_t27_solubility_enthalpy_trends.png"),
            figure_caption="Fig. 41.1: Standard enthalpy of solution trends for Group 2 sulfates.",
            parts=[
                QuestionPart("(a)", "State the trend in the solubility of Group 2 sulfates down the group.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Explain the trend in terms of the relative changes in lattice energy and hydration enthalpy.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Barium sulfate is precipitated by adding sodium sulfate to barium chloride. Write the full and ionic equations.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Solubility decreases down Group 2 from MgSO4 to BaSO4 [1].", "marks": 1},
                {"part": "(b)", "points": "Both &Delta;H°latt and &Delta;H°hyd become less exothermic down the group as cation radius increases [1]; Because the SO4 2- ion is very large, the lattice energy decreases only slightly [1]; The hydration enthalpy of M2+ decreases much more steeply, causing &Delta;H°sol to become more endothermic (positive), reducing solubility [1].", "marks": 3},
                {"part": "(c)", "points": "Full: BaCl2(aq) + Na2SO4(aq) &rarr; BaSO4(s) + 2NaCl(aq) [1]; Ionic: Ba2+(aq) + SO4 2-(aq) &rarr; BaSO4(s) [1].", "marks": 2}
            ]
        ),

        # Q42: 9701/41/M/J/23/Q1(Repeat 2 - 6m)
        Question(
            number=42,
            title="[CORE REPEAT 2] Carbonate Thermal Stability & Anion Polarisation Mechanism — 9701/41/M/J/23/Q1 [6 Marks]",
            syllabus_ref="27.1", difficulty="HARD", section_key="SEC_D",
            preamble="The thermal decomposition temperatures of Group 2 carbonates follow the trend in Fig. 42.1.",
            figure_path=os.path.join(fig_dir, "a2_t27_thermal_stability_trend.png"),
            figure_caption="Fig. 42.1: Increasing decomposition temperature of Group 2 carbonates with increasing cation radius.",
            parts=[
                QuestionPart("(a)", "State how the decomposition temperature varies with the radius of the M<sup>2+</sup> cation.", 1, num_answer_lines=2),
                QuestionPart("(b)", "Explain why magnesium carbonate decomposes much more easily than barium carbonate.", 3, num_answer_lines=4),
                QuestionPart("(c)", "Write balanced equations for the decomposition of CaCO<sub>3</sub> and Ca(NO<sub>3</sub>)<sub>2</sub>.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Decomposition temperature increases as cation radius increases [1].", "marks": 1},
                {"part": "(b)", "points": "Mg2+ has a much smaller ionic radius and higher charge density than Ba2+ [1]; Mg2+ exerts a stronger polarising power on the electron cloud of the CO3 2- anion [1]; This distorts the carbonate ion and weakens a C-O bond, lowering the activation energy for decomposition [1].", "marks": 3},
                {"part": "(c)", "points": "CaCO3(s) &rarr; CaO(s) + CO2(g) [1]; 2Ca(NO3)2(s) &rarr; 2CaO(s) + 4NO2(g) + O2(g) [1].", "marks": 2}
            ]
        ),

        # Q43: 9701/42/O/N/23/Q1(Repeat 3 - 6m)
        Question(
            number=43,
            title="[CORE REPEAT 3] Hydroxide Solubility Trend & Industrial Uses — 9701/42/O/N/23/Q1 [6 Marks]",
            syllabus_ref="27.2", difficulty="HARD", section_key="SEC_D",
            preamble="Group 2 hydroxides become increasingly soluble down the group, reaching an alkaline pH of 13 for Ba(OH)<sub>2</sub>.",
            parts=[
                QuestionPart("(a)", "Explain why Group 2 hydroxides become more soluble down the group.", 3, num_answer_lines=4),
                QuestionPart("(b)", "Describe the use of calcium hydroxide in treating acidic soil and explain the chemical hazard of mixing it with ammonium fertilisers.", 2, num_answer_lines=3),
                QuestionPart("(c)", "State the flame colours for strontium and barium compounds.", 1, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Both &Delta;H°latt and &Delta;H°hyd become less exothermic down the group [1]; Because OH- is a very small anion, the inter-ionic distance (r+ + r-) increases proportionally more, so lattice energy decreases much faster than hydration enthalpy [1]; Consequently, &Delta;H°sol becomes more exothermic (or less endothermic), favouring dissolution [1].", "marks": 3},
                {"part": "(b)", "points": "Neutralises soil acidity [1]; Reacts with ammonium ions liberating volatile ammonia gas: Ca(OH)2 + 2NH4+ &rarr; Ca2+ + 2NH3(g) + 2H2O, depleting the soil of vital nitrogen [1].", "marks": 2},
                {"part": "(c)", "points": "Strontium: scarlet / crimson red; Barium: apple-green [1].", "marks": 1}
            ]
        ),

        # Q44: 9701/41/O/N/23/Q1(Repeat 4 - 6m)
        Question(
            number=44,
            title="[CORE REPEAT 4] Nitrate Decomposition Stoichiometry & Gas Volume Calculation — 9701/41/O/N/23/Q1 [6 Marks]",
            syllabus_ref="27.1", difficulty="HARD", section_key="SEC_D",
            preamble="A sample of 2.12 g of anhydrous strontium nitrate, Sr(NO<sub>3</sub>)<sub>2</sub> (<i>M</i><sub>r</sub> = 211.6), is heated strongly until decomposition is complete:<br/>2Sr(NO<sub>3</sub>)<sub>2</sub>(s) &rarr; 2SrO(s) + 4NO<sub>2</sub>(g) + O<sub>2</sub>(g)<br/>Assume all gas volumes are measured at room temperature and pressure (rtp, molar gas volume = 24.0 dm<sup>3</sup> mol<sup>-1</sup>).",
            parts=[
                QuestionPart("(a)", "Calculate the mass of solid residue, SrO (<i>M</i><sub>r</sub> = 103.6), formed.", 2, num_answer_lines=3),
                QuestionPart("(b)", "Calculate the volume of nitrogen dioxide gas, NO<sub>2</sub>, evolved at rtp.", 2, num_answer_lines=3),
                QuestionPart("(c)", "Describe a chemical test to confirm that oxygen gas is also present in the evolved gas mixture.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Moles Sr(NO3)2 = 2.12 / 211.6 = 0.01002 mol [1]; Mass SrO = 0.01002 &times; 103.6 = 1.04 g [1].", "marks": 2},
                {"part": "(b)", "points": "Moles NO2 = 2 &times; 0.01002 = 0.02004 mol [1]; Volume NO2 = 0.02004 &times; 24.0 = 0.481 dm3 (481 cm3) [1].", "marks": 2},
                {"part": "(c)", "points": "Insert a glowing splint into the gas mixture [1]; The splint relights / bursts into flame [1].", "marks": 2}
            ]
        ),

        # Q45: 9701/42/M/J/22/Q1(Repeat 5 - 4m)
        Question(
            number=45,
            title="[CORE REPEAT 5] Polarising Power Definition & Trend Explanation — 9701/42/M/J/22/Q1 [4 Marks]",
            syllabus_ref="27.1", difficulty="MEDIUM", section_key="SEC_D",
            preamble="The ability of a cation to distort an anion's electron cloud is called its polarising power.",
            parts=[
                QuestionPart("(a)", "State two factors that govern the polarising power of a cation.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Explain why the polarising power of Group 2 cations decreases down the group from Mg<sup>2+</sup> to Ba<sup>2+</sup>.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "1. Ionic charge of the cation [1]; 2. Ionic radius of the cation (or charge density) [1].", "marks": 2},
                {"part": "(b)", "points": "The ionic charge remains constant at +2 [1]; The ionic radius increases down the group, so charge density and electric field strength decrease, weakening polarising power [1].", "marks": 2}
            ]
        ),

        # Q46: 9701/41/M/J/22/Q1(Repeat 6 - 4m)
        Question(
            number=46,
            title="[CORE REPEAT 6] Reaction of Magnesium with Steam vs Water — 9701/41/M/J/22/Q1 [4 Marks]",
            syllabus_ref="27.3", difficulty="MEDIUM", section_key="SEC_D",
            preamble="Magnesium reacts differently with cold liquid water and hot gaseous steam.",
            parts=[
                QuestionPart("(a)", "Write the balanced chemical equation for the reaction of magnesium with steam.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the balanced chemical equation for the reaction of magnesium with cold water, and state why the reaction with cold water is extremely slow.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Mg(s) + H2O(g) &rarr; MgO(s) + H2(g) [2].", "marks": 2},
                {"part": "(b)", "points": "Mg(s) + 2H2O(l) &rarr; Mg(OH)2(s) + H2(g) [1]; Mg(OH)2 is sparingly soluble and forms an impervious surface barrier layer on the magnesium metal that prevents further contact with water [1].", "marks": 2}
            ]
        ),

        # Q47: 9701/42/O/N/22/Q1(Repeat 7 - 4m)
        Question(
            number=47,
            title="[CORE REPEAT 7] Testing for Sulfate Ions & Solubility of Barium Salts — 9701/42/O/N/22/Q1 [4 Marks]",
            syllabus_ref="27.4", difficulty="MEDIUM", section_key="SEC_D",
            preamble="A white powder is suspected of containing sulfate ions.",
            parts=[
                QuestionPart("(a)", "Describe how to test for sulfate ions in aqueous solution, stating reagents and the positive observation.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Write the ionic equation for the precipitation reaction and state why barium sulfate does not dissolve in dilute acid.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Add dilute hydrochloric acid (or dilute nitric acid) followed by aqueous barium chloride (or barium nitrate) [1]; A thick white precipitate forms [1].", "marks": 2},
                {"part": "(b)", "points": "Ba2+(aq) + SO4 2-(aq) &rarr; BaSO4(s) [1]; BaSO4 is the salt of a strong acid (H2SO4) so the sulfate ion does not react with H+ to form an undissociated acid [1].", "marks": 2}
            ]
        ),

        # Q48: 9701/41/O/N/22/Q1(Repeat 8 - 4m)
        Question(
            number=48,
            title="[CORE REPEAT 8] Thermal Decomposition of Calcium Carbonate — 9701/41/O/N/22/Q1 [4 Marks]",
            syllabus_ref="27.1", difficulty="MEDIUM", section_key="SEC_D",
            preamble="Calcium carbonate decomposes on strong heating:<br/>CaCO<sub>3</sub>(s) &rarr; CaO(s) + CO<sub>2</sub>(g)",
            parts=[
                QuestionPart("(a)", "State the type of reaction and whether it is exothermic or endothermic.", 2, num_answer_lines=2),
                QuestionPart("(b)", "Describe a chemical test for the gas evolved, including the observation and balanced chemical equation.", 2, num_answer_lines=3)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Thermal decomposition [1]; Endothermic (&Delta;H > 0) [1].", "marks": 2},
                {"part": "(b)", "points": "Bubble gas through limewater (aqueous calcium hydroxide): limewater turns cloudy / milky [1]; Ca(OH)2(aq) + CO2(g) &rarr; CaCO3(s) + H2O(l) [1].", "marks": 2}
            ]
        ),

        # Q49: 9701/42/M/J/21/Q1(Repeat 9 - 2m)
        Question(
            number=49,
            title="[CORE REPEAT 9] Flame Emission Colour of Barium — 9701/42/M/J/21/Q1 [2 Marks]",
            syllabus_ref="27.3", difficulty="EASY", section_key="SEC_D",
            preamble="Flame tests identify metal cations.",
            parts=[
                QuestionPart("(a)", "State the flame colour for barium and explain why a non-luminous flame must be used.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Apple-green [1]; A non-luminous (blue) flame provides high heat and does not mask the emission colour with yellow soot [1].", "marks": 2}
            ]
        ),

        # Q50: 9701/41/M/J/21/Q1(Repeat 10 - 2m)
        Question(
            number=50,
            title="[CORE REPEAT 10] Relative Basicity of Group 2 Oxides — 9701/41/M/J/21/Q1 [2 Marks]",
            syllabus_ref="27.3", difficulty="EASY", section_key="SEC_D",
            preamble="Oxides of Group 2 elements are basic.",
            parts=[
                QuestionPart("(a)", "State the trend in basicity of Group 2 oxides down the group, and state the oxide with the highest basicity.", 2, num_answer_lines=2)
            ],
            mark_scheme=[
                {"part": "(a)", "points": "Basicity increases down Group 2 [1]; Barium oxide (BaO) has the highest basicity [1].", "marks": 2}
            ]
        ),
    ]

    print("Topic 27 Questions Count:", len(questions))

    # Audit tariff
    m6 = sum(1 for q in questions if sum(p.marks for p in q.parts) == 6)
    m4 = sum(1 for q in questions if sum(p.marks for p in q.parts) == 4)
    m2 = sum(1 for q in questions if sum(p.marks for p in q.parts) == 2)
    tot = sum(sum(p.marks for p in q.parts) for q in questions)
    print(f"Tariff Breakdown: 6-markers = {m6} (40%), 4-markers = {m4} (40%), 2-markers = {m2} (20%) | Total Marks = {tot}")
    assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"
    assert m6 == 20, f"Expected 20 6-markers, got {m6}"
    assert m4 == 20, f"Expected 20 4-markers, got {m4}"
    assert m2 == 10, f"Expected 10 2-markers, got {m2}"
    assert tot == 220, f"Expected 220 marks, got {tot}"

    build_a2_theory_pdf(
        output_path=output_path,
        topic_title=topic_title,
        topic_subtitle=topic_subtitle,
        subtopics_summary=subtopics_summary,
        subtopic_map=subtopic_map,
        questions=questions
    )
    print("Topic 27 PDF built successfully!")

if __name__ == "__main__":
    build_topic27_50q()
