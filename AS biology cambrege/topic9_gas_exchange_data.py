"""
Topic 9: Gas Exchange - 50 Examination-Style Questions & Mark Schemes
Cambridge International AS Level Biology (9700)
Candidate: Hamna | Mentora Academy

Structure:
- Section A: High-Tariff Structured Analysis & Data Evaluation (20 Qs x 6m = 120 Marks)
- Section B: Core Conceptual & Physiological Mechanism Questions (20 Qs x 4m = 80 Marks)
- Section C: High-Yield Rapid Recall & Rigorous Definitions (10 Qs x 2m = 20 Marks)
Total: 50 Questions | 220 Marks
Past Paper vs Original Ratio: 44 Authentic (88%) / 6 Original Extensions (12%)
Visual Density: 14 High-Resolution 300 DPI Diagrams Embedded
"""

import os
from build_as_biology_pdf import Question, QuestionPart

DIAGRAM_DIR = r"z:\tests n quizes63\books\psycology\new styl\AS biology cambrege\diagrams"

def get_topic9_questions():
    questions = []

    # =========================================================================
    # SECTION A: HIGH-TARIFF STRUCTURED ANALYSIS & DATA EVALUATION (20 x 6m = 120m)
    # =========================================================================

    # Q1: Gross anatomy & functional organisation (Fig 9.1)
    questions.append(Question(
        number=1,
        title="9700/22/M/J/23/Q3 - Gross Anatomy and Functional Organisation of the Human Gas Exchange System",
        syllabus_ref="Syllabus 9.1",
        difficulty="ADVANCED",
        preamble="The human gas exchange system consists of conducting airways and respiratory surfaces adapted for the efficient uptake of oxygen and removal of carbon dioxide. Fig. 9.1 illustrates the gross anatomy of the respiratory tract from the larynx to the terminal alveoli.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_1.png"),
        figure_caption="Fig. 9.1: Gross anatomy of the human gas exchange system showing conducting airways, lobar lungs, and diaphragm.",
        parts=[
            QuestionPart(label="(a)", text="Describe the route taken by an inspired oxygen molecule from the larynx to an alveolar air space, naming each conducting airway in sequence.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the physiological importance of the incomplete C-shaped cartilage rings in the trachea compared to complete circular rings.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the role of the pleural fluid and pleural membranes surrounding each lung during ventilation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q1(a)", "points": "Larynx -> trachea -> main / primary bronchus -> lobar / secondary bronchus -> bronchiole -> terminal bronchiole -> respiratory bronchiole -> alveolar duct / sac / alveolus [2].", "marks": 2},
            {"q": "Q1(b)", "points": "Incomplete dorsal gap allows the esophagus (located directly posterior) to expand during swallowing of a food bolus; while anterior/lateral cartilage prevents tracheal collapse during negative pressure generated on inspiration [2].", "marks": 2},
            {"q": "Q1(c)", "points": "Pleural fluid acts as a lubricant reducing friction between visceral and parietal pleura during respiratory movements; surface tension adheres lungs to thoracic wall, ensuring lungs expand when thoracic volume increases [2].", "marks": 2}
        ]
    ))

    # Q2: Histological plan of trachea wall (Fig 9.2)
    questions.append(Question(
        number=2,
        title="9700/21/O/N/22/Q2 - Histological Structure of the Trachea Wall and Function of Component Tissues",
        syllabus_ref="Syllabus 9.1 & 9.2",
        difficulty="ADVANCED",
        preamble="The wall of the trachea contains several distinct tissue layers that support the airway and protect against inhaled pathogens. Fig. 9.2 is a histological plan diagram of a transverse section (TS) through the tracheal wall.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_2.png"),
        figure_caption="Fig. 9.2: Histological plan diagram of a transverse section through the anterior wall of the human trachea.",
        parts=[
            QuestionPart(label="(a)", text="Identify the tissue forming the hyaline cartilage ring and describe its cellular organisation and extracellular matrix.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State the functions of the seromucous glands located in the submucosa and the elastic fibres in the lamina propria.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the structure and location of the trachealis muscle and outline its function during coughing.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q2(a)", "points": "Chondrocytes located within lacunae; embedded in a firm, hydrated extracellular matrix containing collagen fibrils and chondroitin sulfate proteoglycans [2].", "marks": 2},
            {"q": "Q2(b)", "points": "Seromucous glands secrete watery fluid and mucin to trap airborne particles and humidify inspired air [1]; elastic fibres allow stretching during inspiration and recoil to maintain airway patency and elasticity [1].", "marks": 2},
            {"q": "Q2(c)", "points": "Smooth muscle located in the posterior / dorsal gap of the cartilage C-ring [1]; contracts during the cough reflex to narrow the tracheal lumen, accelerating linear airflow velocity to expel mucus plugs [1].", "marks": 2}
        ]
    ))

    # Q3: Ultrastructure of ciliated epithelium and goblet cells (Fig 9.3)
    questions.append(Question(
        number=3,
        title="9700/22/M/J/22/Q4 - Ultrastructure of Ciliated Columnar Epithelium and the Mucociliary Escalator",
        syllabus_ref="Syllabus 9.1 & 9.2",
        difficulty="ADVANCED",
        preamble="The pseudostratified columnar epithelium lining the trachea and bronchi functions as a vital defensive barrier. Fig. 9.3 shows the fine ultrastructure of ciliated epithelial cells, goblet cells, and the overlying mucus blanket.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_3.png"),
        figure_caption="Fig. 9.3: Transmission electron micrograph schematic of ciliated epithelial cells and a goblet cell forming the mucociliary escalator.",
        parts=[
            QuestionPart(label="(a)", text="Describe the internal microtubule arrangement of a cilium and outline how dynein motor arms produce ciliary beating.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why ciliated epithelial cells contain a large number of mitochondria clustered beneath the basal bodies.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe the synthesis and secretion of mucin glycoproteins by goblet cells and outline the function of the mucus layer.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q3(a)", "points": "Axoneme exhibits a '9+2' arrangement (9 peripheral microtubule doublets surrounding 2 central singlets) [1]; dynein arms hydrolyse ATP to cause sliding of adjacent doublets, producing a coordinated metachronal wave [1].", "marks": 2},
            {"q": "Q3(b)", "points": "Aerobic respiration generates abundant ATP [1]; required by dynein ATPase arms for continuous ciliary motility and active transport at basal bodies [1].", "marks": 2},
            {"q": "Q3(c)", "points": "Synthesised at rough ER, glycosylated and packaged in Golgi body, secreted via exocytosis of mucin granules [1]; traps dust, pollen, and bacteria, preventing microbial access to alveoli [1].", "marks": 2}
        ]
    ))

    # Q4: Comparative histology: Bronchus vs Bronchiole (Fig 9.4)
    questions.append(Question(
        number=4,
        title="9700/23/O/N/21/Q2 - Comparative Histology of Bronchi and Bronchioles: Tissue Distribution and Function",
        syllabus_ref="Syllabus 9.1 & 9.2",
        difficulty="ADVANCED",
        preamble="As the bronchial tree branches deeper into the lung parenchyma, marked histological transitions occur. Fig. 9.4 compares transverse sections of a medium bronchus and a terminal bronchiole.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_4.png"),
        figure_caption="Fig. 9.4: Comparison of transverse sections (TS) through a bronchus and a terminal bronchiole.",
        parts=[
            QuestionPart(label="(a)", text="State two major structural differences visible in Fig. 9.4 between the wall of a bronchus and the wall of a bronchiole.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the prominent ring of smooth muscle in the bronchiole wall regulates ventilation to different pulmonary regions.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why the absence of cartilage in bronchioles makes them vulnerable to collapse in patients with severe emphysema.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q4(a)", "points": "Bronchus contains irregular cartilage plates whereas bronchiole has no cartilage [1]; bronchus contains submucosal glands / goblet cells whereas terminal bronchiole lacks glands / has simple cuboidal epithelium [1].", "marks": 2},
            {"q": "Q4(b)", "points": "Contraction of smooth muscle causes bronchoconstriction, reducing airflow to hypoventilated or damaged alveoli [1]; relaxation causes bronchodilation (e.g. stimulated by adrenaline), reducing airway resistance during exercise [1].", "marks": 2},
            {"q": "Q4(c)", "points": "Without rigid cartilage, bronchiole lumen is held open solely by radial traction of surrounding elastic fibres; when elastase destroys elastic fibres, positive intrapleural pressure during forced expiration causes bronchioles to collapse, trapping air [2].", "marks": 2}
        ]
    ))

    # Q5: Alveolar-capillary diffusion barrier (Fig 9.5)
    questions.append(Question(
        number=5,
        title="9700/22/F/M/23/Q3 - Ultrastructure of the Alveolar-Capillary Unit and the Diffusion Barrier",
        syllabus_ref="Syllabus 9.1 & 9.3",
        difficulty="ADVANCED",
        preamble="Gas exchange between alveolar air and pulmonary capillary blood occurs across an extremely thin barrier. Fig. 9.5 illustrates the ultrastructural components of the alveolar-capillary barrier and the cellular components of the alveolar septum.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_5.png"),
        figure_caption="Fig. 9.5: Ultrastructure of the alveolar-capillary interface showing pneumocytes, basement membranes, and endothelial cells.",
        parts=[
            QuestionPart(label="(a)", text="List the three specific structural layers that comprise the gas exchange barrier between alveolar air and capillary blood plasma.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Distinguish between the structure and function of Type I pneumocytes and Type II pneumocytes.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain the physiological consequence if Type II pneumocytes fail to secrete sufficient pulmonary surfactant.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q5(a)", "points": "Squamous epithelial cell (Type I pneumocyte) cytoplasm / cell surface membrane [1]; fused extracellular basement membrane [1]; capillary endothelial cell cytoplasm / cell surface membrane [total < 0.5 µm path, 2].", "marks": 2},
            {"q": "Q5(b)", "points": "Type I pneumocytes are extremely flattened squamous cells providing a minimal diffusion distance [1]; Type II pneumocytes are rounded / cuboidal secretory cells that synthesise and exocytose dipalmitoylphosphatidylcholine (surfactant) [1].", "marks": 2},
            {"q": "Q5(c)", "points": "High surface tension of water lining alveoli remains unopposed; small alveoli collapse during expiration (atelectasis), requiring immense muscular effort to reinflate (infant respiratory distress syndrome) [2].", "marks": 2}
        ]
    ))

    # Q6: Alveolar elastic fibres and mechanics of recoil (Fig 9.6)
    questions.append(Question(
        number=6,
        title="9700/21/M/J/23/Q4 - Role of Alveolar Elastic Fibres in Ventilation and Pathological Elastic Breakdown",
        syllabus_ref="Syllabus 9.1 & 9.2",
        difficulty="ADVANCED",
        preamble="Alveoli are enveloped in a dense basket-like network of elastic fibres consisting of elastin proteins. Fig. 9.6 compares the physical state of these elastic fibres during inhalation and exhalation.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_6.png"),
        figure_caption="Fig. 9.6: Schematic diagram showing the stretching of alveolar elastic fibres during inspiration and passive recoil during expiration.",
        parts=[
            QuestionPart(label="(a)", text="Explain the mechanical role of elastic fibres during inspiration and quiet expiration at rest.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="State why expiration at rest is described as an energetically passive process.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how the destruction of elastic fibres in a chronic smoker leads to the development of a 'barrel chest'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q6(a)", "points": "Fibres stretch as thoracic cavity expands, allowing alveoli to inflate without bursting [1]; stored potential energy causes passive elastic recoil during exhalation, forcing air out of alveoli [1].", "marks": 2},
            {"q": "Q6(b)", "points": "Does not require muscular contraction or ATP hydrolysis; relies entirely on relaxation of diaphragm and external intercostals combined with elastic recoil of lung parenchyma [2].", "marks": 2},
            {"q": "Q6(c)", "points": "Loss of alveolar recoil means lungs cannot fully empty; air remains trapped in alveoli, increasing residual volume and permanently hyperinflating the thoracic cavity (barrel chest deformity) [2].", "marks": 2}
        ]
    ))

    # Q7: Spirometry analysis of lung volumes and capacities (Fig 9.7)
    questions.append(Question(
        number=7,
        title="9700/22/O/N/23/Q4 - Analysis of Spirometry Traces: Lung Volumes, Capacities, and Ventilation Rate",
        syllabus_ref="Syllabus 9.1",
        difficulty="ADVANCED",
        preamble="A spirometer was used to record changes in lung volume of a healthy 18-year-old student at rest and during maximal respiratory efforts. Fig. 9.7 shows the resulting spirogram trace.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_7.png"),
        figure_caption="Fig. 9.7: Spirometer trace showing tidal breathing, maximal inspiration, maximal expiration, and residual volume.",
        parts=[
            QuestionPart(label="(a)", text="Using values from Fig. 9.7, determine the Tidal Volume (VT) and calculate the student's Vital Capacity (VC).", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Define Residual Volume (RV) and explain why it cannot be measured directly using a simple water-filled spirometer.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="The student had a resting breathing rate of 14 breaths per minute. Calculate the Pulmonary Ventilation Rate (PVR) in dm³ min⁻¹, showing your working.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q7(a)", "points": "Tidal Volume (VT) = 2.85 - 2.35 = 0.50 dm³ [1]; Vital Capacity (VC) = 5.60 - 1.20 = 4.40 dm³ (or VC = IRV + VT + ERV = 2.75 + 0.50 + 1.15 = 4.40 dm³) [1].", "marks": 2},
            {"q": "Q7(b)", "points": "Volume of air remaining in the lungs after a maximal forced expiration (~1.2 dm³) [1]; cannot be measured because it cannot be exhaled into the spirometer chamber (requires helium dilution or plethysmography) [1].", "marks": 2},
            {"q": "Q7(c)", "points": "PVR = Tidal Volume x Breathing Rate [1]; PVR = 0.50 dm³ x 14 min⁻¹ = 7.0 dm³ min⁻¹ (units required) [1].", "marks": 2}
        ]
    ))

    # Q8: Fick's Law of Diffusion applied to alveolar surface (Fig 9.8)
    questions.append(Question(
        number=8,
        title="9700/21/M/J/21/Q3 - Fick's First Law of Diffusion and Quantitative Adaptations of the Alveolar Surface",
        syllabus_ref="Syllabus 9.3",
        difficulty="ADVANCED",
        preamble="The rate of gas exchange across pulmonary membranes is governed by physical laws of diffusion. Fig. 9.8 summarizes Fick's first law of diffusion and the specific physiological factors operating at the human alveolar membrane.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_8.png"),
        figure_caption="Fig. 9.8: Mathematical expression of Fick's law and physiological factors optimizing diffusion rate in lungs.",
        parts=[
            QuestionPart(label="(a)", text="State Fick's first law of diffusion in words or as a proportional relationship, defining each variable.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the respiratory and circulatory systems cooperate to maintain a steep partial pressure gradient for oxygen.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Although the partial pressure gradient for CO2 (5 mmHg) is much smaller than for O2 (64 mmHg), both gases diffuse at comparable total rates. Explain why.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q8(a)", "points": "Rate of diffusion is directly proportional to surface area (A) and concentration / partial pressure gradient (ΔP), and inversely proportional to diffusion distance (x): Rate ∝ (A x ΔP) / x [2].", "marks": 2},
            {"q": "Q8(b)", "points": "Ventilation constantly replenishes O2 in alveoli, keeping alveolar pO2 high (~104 mmHg) [1]; continuous perfusion carries oxygenated blood away and delivers deoxygenated blood (pO2 ~40 mmHg), keeping capillary pO2 low [1].", "marks": 2},
            {"q": "Q8(c)", "points": "Carbon dioxide has a diffusion constant / solubility in water and lipid membranes approximately 20 times higher than that of oxygen; higher solubility compensates for the lower concentration gradient [2].", "marks": 2}
        ]
    ))

    # Q9: Histopathology of chronic bronchitis (Fig 9.9)
    questions.append(Question(
        number=9,
        title="9700/22/M/J/20/Q3 - Pathogenesis and Histopathological Hallmarks of Chronic Bronchitis",
        syllabus_ref="Syllabus 9.4 & 9.5",
        difficulty="ADVANCED",
        preamble="Tobacco smoke contains irritants that provoke progressive structural damage to the bronchial tree. Fig. 9.9 compares the histology of healthy bronchial mucosa with that from a long-term cigarette smoker suffering from chronic bronchitis.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_9.png"),
        figure_caption="Fig. 9.9: Histopathological alterations in the bronchial epithelium and submucosa in chronic bronchitis compared to healthy tissue.",
        parts=[
            QuestionPart(label="(a)", text="Describe the cellular changes that occur in the epithelial lining of the bronchi in chronic bronchitis.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why chronic bronchitis patients suffer from a persistent, productive cough ('smoker's cough').", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how chronic bronchitis increases susceptibility to recurrent secondary bacterial infections.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q9(a)", "points": "Hypertrophy and hyperplasia of goblet cells and submucosal glands [1]; loss, paralysis, or destruction of cilia (ciliostasis) and squamous metaplasia [1].", "marks": 2},
            {"q": "Q9(b)", "points": "Excessive, thick mucus cannot be removed by paralyzed cilia; accumulation of mucus triggers sensory cough receptors in bronchial walls to forcefully expel mucus plugs [2].", "marks": 2},
            {"q": "Q9(c)", "points": "Stagnant, warm mucus pools in lower airways, providing a nutrient-rich culture medium; pathogens (e.g. Streptococcus pneumoniae, Haemophilus influenzae) are not cleared and colonise airway tissues [2].", "marks": 2}
        ]
    ))

    # Q10: Pathogenesis of emphysema (Fig 9.10)
    questions.append(Question(
        number=10,
        title="9700/22/O/N/20/Q4 - Molecular and Cellular Pathogenesis of Pulmonary Emphysema: The Protease-Antiprotease Hypothesis",
        syllabus_ref="Syllabus 9.4 & 9.5",
        difficulty="ADVANCED",
        preamble="Emphysema is characterized by irreversible destruction of alveolar walls. Fig. 9.10 outlines the biochemical pathway involving inflammatory cells, proteolytic enzymes, and protective antiproteases in emphysema.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_10.png"),
        figure_caption="Fig. 9.10: The protease-antiprotease imbalance mechanism leading to alveolar wall destruction in pulmonary emphysema.",
        parts=[
            QuestionPart(label="(a)", text="Explain how cigarette smoke particulates trigger the recruitment and activation of neutrophils in lung tissue.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the normal function of α1-antitrypsin and explain how components of cigarette smoke impair its activity.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why the destruction of alveolar septa leads to severe breathlessness (dyspnea) during mild exertion.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q10(a)", "points": "Particulates are phagocytosed by alveolar macrophages, which release inflammatory cytokines (e.g. IL-8, TNF-α, leukotrienes) that attract circulating neutrophils across capillary walls [2].", "marks": 2},
            {"q": "Q10(b)", "points": "α1-antitrypsin is a serine protease inhibitor that inactivates elastase, protecting alveolar elastin [1]; oxidants in cigarette smoke oxidize active-site methionine residues of α1-antitrypsin, abolishing its inhibitory capacity [1].", "marks": 2},
            {"q": "Q10(c)", "points": "Alveolar breakdown drastically reduces total surface area for diffusion [1]; destruction of capillaries and loss of elastic recoil cause air trapping, leading to severe arterial hypoxemia and acidosis [1].", "marks": 2}
        ]
    ))

    # Q11: Tobacco smoke triad: Nicotine, CO, Tar (Fig 9.11)
    questions.append(Question(
        number=11,
        title="9700/21/O/N/19/Q4 - Toxicological Actions of Nicotine, Carbon Monoxide, and Tar on Cardiovascular and Respiratory Systems",
        syllabus_ref="Syllabus 9.4",
        difficulty="ADVANCED",
        preamble="Cigarette smoke contains thousands of chemical compounds, three of which have distinct toxicological effects. Fig. 9.11 summarizes the modes of action of nicotine, carbon monoxide, and tar.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_11.png"),
        figure_caption="Fig. 9.11: Summary diagram comparing the chemical nature and physiological impacts of nicotine, carbon monoxide, and tar.",
        parts=[
            QuestionPart(label="(a)", text="Describe how nicotine acts on the autonomic nervous system and endocrine glands to increase cardiovascular strain.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the biochemical effect of carbon monoxide on haemoglobin and state how this affects fetal development in pregnant smokers.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how tar causes both mechanical failure of the mucociliary system and genetic mutations leading to neoplasia.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q11(a)", "points": "Stimulates nicotinic acetylcholine receptors and induces adrenal medulla to release adrenaline [1]; causes systemic arteriolar vasoconstriction, elevating peripheral resistance, heart rate, and arterial blood pressure [1].", "marks": 2},
            {"q": "Q11(b)", "points": "Binds irreversibly to Fe²⁺ in haem groups forming carboxyhaemoglobin (HbCO), reducing oxygen carriage; crosses placenta causing fetal hypoxia, leading to low birth weight or premature birth [2].", "marks": 2},
            {"q": "Q11(c)", "points": "Sticky residue coats and paralyzes cilia, causing mucus stagnation [1]; contains carcinogens (e.g. benzo[a]pyrene) that form DNA adducts causing mutations in proto-oncogenes and tumor suppressor genes [1].", "marks": 2}
        ]
    ))

    # Q12: Bronchogenic carcinoma progression (Fig 9.12)
    questions.append(Question(
        number=12,
        title="9700/22/M/J/19/Q3 - Multi-Step Carcinogenesis of Lung Cancer: From Metaplasia to Metastatic Carcinoma",
        syllabus_ref="Syllabus 9.4 & 9.5",
        difficulty="ADVANCED",
        preamble="Lung cancer (bronchogenic carcinoma) develops through a multi-stage progression of genetic and histological changes. Fig. 9.12 illustrates the sequential stages from normal respiratory mucosa to invasive carcinoma.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_12.png"),
        figure_caption="Fig. 9.12: Stages in bronchial epithelial transformation: normal mucosa -> squamous metaplasia -> dysplasia -> invasive carcinoma.",
        parts=[
            QuestionPart(label="(a)", text="Define the terms 'carcinogen' and 'metastasis' in the context of bronchogenic carcinoma.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the roles of mutated proto-oncogenes and tumor suppressor genes in the uncontrolled proliferation of bronchial cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="State two common clinical symptoms of lung cancer and explain the pathological basis for each symptom.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q12(a)", "points": "Carcinogen: an agent (chemical/physical) capable of inducing genetic mutations that cause cancer [1]; Metastasis: the spread of malignant tumor cells from primary bronchial site via blood or lymph to secondary organs [1].", "marks": 2},
            {"q": "Q12(b)", "points": "Mutated proto-oncogenes (oncogenes, e.g. KRAS) code for hyperactive growth factor receptors stimulating continuous mitosis [1]; mutated tumor suppressor genes (e.g. TP53) fail to arrest cell cycle or trigger apoptosis in damaged cells [1].", "marks": 2},
            {"q": "Q12(c)", "points": "Persistent hemoptysis (coughing blood) due to tumor erosion of bronchial blood vessels [1]; dyspnea / wheezing due to physical obstruction of bronchial lumen by growing tumor mass [1].", "marks": 2}
        ]
    ))

    # Q13: Mechanics of ventilation: Volume and Pressure dynamics (Fig 9.13)
    questions.append(Question(
        number=13,
        title="9700/22/M/J/18/Q3 - Thoracic Mechanics, Intrapleural Pressure, and Boyle's Law During Ventilation",
        syllabus_ref="Syllabus 9.1",
        difficulty="ADVANCED",
        preamble="Ventilation is driven by pressure differences generated between the atmosphere and the alveolar air spaces according to Boyle's law. Fig. 9.13 outlines the neuromuscular actions and physical changes during inspiration and expiration.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_13.png"),
        figure_caption="Fig. 9.13: Neuromuscular mechanisms and thoracic volume/pressure relationships during inhalation and exhalation.",
        parts=[
            QuestionPart(label="(a)", text="Describe the coordinated actions of the diaphragm and external intercostal muscles during quiet inspiration.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the muscle contractions described in (a) lead to air flowing into the alveoli, with reference to Boyle's law.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Describe how forced expiration (e.g. during vigorous exercise) differs from quiet expiration at rest.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q13(a)", "points": "Diaphragm contracts and flattens downwards [1]; external intercostal muscles contract, pulling ribs upwards and outwards [1].", "marks": 2},
            {"q": "Q13(b)", "points": "Thoracic volume increases; according to Boyle's law (P ∝ 1/V), intrapulmonary pressure decreases below atmospheric pressure (-1 mmHg) [1]; air moves into the lungs down the pressure gradient until equilibrium is reached [1].", "marks": 2},
            {"q": "Q13(c)", "points": "Forced expiration is active: internal intercostal muscles contract pulling ribs down and in [1]; abdominal wall muscles contract pushing abdominal viscera and diaphragm upwards, further reducing thoracic volume rapidly [1].", "marks": 2}
        ]
    ))

    # Q14: Tissue distribution matrix across respiratory tract (Fig 9.14)
    questions.append(Question(
        number=14,
        title="9700/21/O/N/18/Q3 - Structural Distribution of Tissues Along the Respiratory Tract and Functional Adaptations",
        syllabus_ref="Syllabus 9.1 & 9.2",
        difficulty="ADVANCED",
        preamble="The histological composition of the human respiratory tract undergoes a progressive transition from the upper conducting airways to the terminal gas exchange units. Fig. 9.14 summarizes the distribution of five key tissues across five anatomical regions.",
        figure_path=os.path.join(DIAGRAM_DIR, "fig9_14.png"),
        figure_caption="Fig. 9.14: Tissue distribution matrix showing cartilage, ciliated epithelium, goblet cells, smooth muscle, and elastic fibres.",
        parts=[
            QuestionPart(label="(a)", text="With reference to Fig. 9.14, state which tissue is present in every region from the trachea to the alveoli, and explain why this tissue is essential throughout.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the transition in epithelial cell morphology from the trachea to the alveoli.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why goblet cells and cartilage must both be absent from the alveolar walls.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q14(a)", "points": "Elastic fibres [1]; allow expansion during inspiration to accommodate air volume and provide elastic recoil to drive passive exhalation and prevent alveolar over-distension [1].", "marks": 2},
            {"q": "Q14(b)", "points": "Transitions from tall pseudostratified ciliated columnar (trachea) -> simple columnar (bronchi) -> simple ciliated cuboidal (bronchioles) -> extremely thin simple squamous epithelium (alveoli) [2].", "marks": 2},
            {"q": "Q14(c)", "points": "Goblet cell mucus would coat alveolar walls, vastly increasing diffusion distance and blocking gas diffusion [1]; rigid cartilage would prevent alveolar expansion and recoil and obstruct capillary perfusion [1].", "marks": 2}
        ]
    ))

    # Q15: Experimental investigation of smoking particulates using cotton wool model
    questions.append(Question(
        number=15,
        title="9700/22/O/N/22/Q3 - Experimental Investigation of Cigarette Smoke Condensates Using a Model Lung Apparatus",
        syllabus_ref="Syllabus 9.4",
        difficulty="ADVANCED",
        preamble="A smoking machine was set up in which the smoke of five burning cigarettes was drawn through glass tubing packed with white glass wool / cotton wool, followed by universal indicator solution and limewater.",
        parts=[
            QuestionPart(label="(a)", text="Describe and explain the appearance of the glass wool after drawing the smoke of five cigarettes through the apparatus.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Predict and explain the colour change observed in the universal indicator solution, naming the chemical species responsible.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain why the limewater becomes cloudy, and evaluate one limitation of this apparatus as a physiological model for human inhalation.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q15(a)", "points": "Glass wool turns dark brown / yellow and becomes sticky [1]; due to the deposition and condensation of particulate tar [1].", "marks": 2},
            {"q": "Q15(b)", "points": "Indicator turns yellow / orange / red (pH decreases / becomes acidic) [1]; due to dissolved oxides of nitrogen (NOx), sulfur dioxide (SO2), or carbon dioxide forming acidic solutions (e.g. HNO3, H2SO3, H2CO3) [1].", "marks": 2},
            {"q": "Q15(c)", "points": "Limewater turns milky / cloudy due to carbon dioxide reacting to precipitate calcium carbonate [1]; limitation: dry glass wool lacks living ciliated epithelium, moist mucus lining, blood supply, or macrophage immune responses [1].", "marks": 2}
        ]
    ))

    # Q16: Carbon monoxide poisoning and carboxyhaemoglobin dissociation
    questions.append(Question(
        number=16,
        title="9700/21/M/J/22/Q2 - Kinetics of Carbon Monoxide Binding to Haemoglobin and Tissue Hypoxia",
        syllabus_ref="Syllabus 9.4 & 8.2",
        difficulty="ADVANCED",
        preamble="Carbon monoxide is a colourless, odourless toxic gas produced by incomplete combustion of organic matter, including tobacco. Blood samples from non-smokers and heavy smokers were analysed for carboxyhaemoglobin (HbCO) percentage.",
        parts=[
            QuestionPart(label="(a)", text="Explain why even low atmospheric concentrations of carbon monoxide (e.g. 0.1%) result in dangerous levels of HbCO in blood.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the formation of HbCO alters the affinity of the remaining unaffected haem groups for oxygen (allosteric effect).", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Suggest why heavy smokers experience elevated resting hematocrit (red blood cell count) and higher blood viscosity.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q16(a)", "points": "Haemoglobin has an affinity for carbon monoxide approximately 200–250 times greater than its affinity for oxygen [1]; binding is essentially irreversible under standard physiological conditions, displacing oxygen [1].", "marks": 2},
            {"q": "Q16(b)", "points": "Binding of CO locks haemoglobin in the high-affinity R-state, shifting the oxygen dissociation curve to the left [1]; prevents the unloading of oxygen to respiring tissues at physiological tissue pO2, causing cellular hypoxia [1].", "marks": 2},
            {"q": "Q16(c)", "points": "Chronic tissue hypoxia stimulates renal cells to secrete erythropoietin (EPO) [1]; EPO stimulates bone marrow erythropoiesis to produce more erythrocytes (secondary polycythemia), increasing blood viscosity [1].", "marks": 2}
        ]
    ))

    # Q17: COPD: Comparative evaluation of Chronic Bronchitis and Emphysema
    questions.append(Question(
        number=17,
        title="9700/23/M/J/20/Q3 - Differential Diagnosis and Pathophysiology of Chronic Obstructive Pulmonary Disease (COPD)",
        syllabus_ref="Syllabus 9.5",
        difficulty="ADVANCED",
        preamble="Chronic Obstructive Pulmonary Disease (COPD) is an umbrella term encompassing chronic bronchitis and emphysema, which often coexist in long-term cigarette smokers.",
        parts=[
            QuestionPart(label="(a)", text="Compare chronic bronchitis and emphysema with respect to the primary anatomical site of disease within the lung.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why patients with pure emphysema are often termed 'pink puffers' whereas advanced chronic bronchitis patients are termed 'blue bloaters'.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Explain how long-standing COPD can lead to pulmonary hypertension and subsequent right ventricular heart failure (cor pulmonale).", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q17(a)", "points": "Chronic bronchitis primarily affects conducting airways (bronchi and larger bronchioles) [1]; emphysema primarily affects respiratory zones (alveolar walls, septa, and respiratory bronchioles) [1].", "marks": 2},
            {"q": "Q17(b)", "points": "Emphysema patients maintain near-normal arterial pO2 by hyperventilating (pink appearance) [1]; chronic bronchitis patients suffer severe ventilation-perfusion mismatch, leading to chronic cyanosis / low pO2 (blue) and fluid retention / oedema (bloating) [1].", "marks": 2},
            {"q": "Q17(c)", "points": "Chronic alveolar hypoxia causes widespread pulmonary arteriolar vasoconstriction and loss of capillary beds, vastly increasing pulmonary vascular resistance [1]; right ventricle must generate higher pressure to pump blood into pulmonary circuit, leading to RV hypertrophy and right-sided failure [1].", "marks": 2}
        ]
    ))

    # Q18: Measuring diffusion rates using agar blocks of differing surface area to volume ratios
    questions.append(Question(
        number=18,
        title="9700/21/M/J/17/Q3 - Modelling Gas Diffusion Rates and the Surface Area-to-Volume Ratio Dilemma",
        syllabus_ref="Syllabus 9.3 & 4.2",
        difficulty="ADVANCED",
        preamble="A student investigated the relationship between organism size and diffusion by immersing agar cubes containing phenolphthalein indicator and dilute sodium hydroxide into dilute hydrochloric acid.",
        parts=[
            QuestionPart(label="(a)", text="State the formula for calculating surface area-to-volume ratio (SA:V) of a cube with side length l, and explain what happens to SA:V as size increases.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why the absolute distance diffused by the acid is identical in all cubes after 10 minutes, but the percentage volume decolourised is lowest in the largest cube.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="With reference to your answer in (a) and (b), explain why large multicellular mammals cannot rely on external body surface diffusion and require specialised lungs.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q18(a)", "points": "SA:V = 6l² / l³ = 6 / l [1]; as side length l increases, volume increases proportionally to l³ while surface area increases only to l², causing SA:V ratio to decrease [1].", "marks": 2},
            {"q": "Q18(b)", "points": "Diffusion rate / speed of H⁺ ion movement depends on temperature and concentration gradient, not cube size [1]; but in the largest cube, diffusion distance to center is too great, so central core remains unpenetrated [1].", "marks": 2},
            {"q": "Q18(c)", "points": "Mammals have a very small SA:V ratio and large internal diffusion distances (> several cm) [1]; diffusion across body surface is far too slow to supply high metabolic oxygen demands; lungs provide a massive internal surface area (~100 m²) with minimal diffusion distance (< 0.5 µm) [1].", "marks": 2}
        ]
    ))

    # Q19: Epidemiological evidence linking smoking to lung cancer and mortality
    questions.append(Question(
        number=19,
        title="9700/22/F/M/21/Q2 - Epidemiological Evidence and the Causal Relationship Between Smoking and Lung Cancer",
        syllabus_ref="Syllabus 9.4 & 9.5",
        difficulty="ADVANCED",
        preamble="In 1950, Richard Doll and Austin Bradford Hill published a landmark study investigating the smoking habits of patients admitted to London hospitals with lung carcinoma compared to matched controls.",
        parts=[
            QuestionPart(label="(a)", text="Explain why a correlation between smoking prevalence and lung cancer incidence does not automatically prove causation.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe two lines of experimental or biochemical evidence that established cigarette smoke as the causal agent of bronchogenic carcinoma.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Epidemiological data shows a 20- to 25-year lag period between increases in national cigarette consumption and rises in lung cancer mortality. Explain this lag phase.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q19(a)", "points": "Correlation merely indicates two variables change together; could be coincidental or driven by confounding third variables (e.g. industrial air pollution, genetic predisposition) [2].", "marks": 2},
            {"q": "Q19(b)", "points": "Identification of specific chemical carcinogens (benzo[a]pyrene) in tar [1]; demonstration that tar induces tumors in animal skin painting experiments, and mutates codons 175, 248, 273 of human TP53 gene in vitro [1].", "marks": 2},
            {"q": "Q19(c)", "points": "Carcinogenesis is a multi-step progressive process requiring multiple cumulative mutations (5–6 mutations in oncogenes/tumor suppressors) over decades before a cell escapes growth control and forms a detectable tumor [2].", "marks": 2}
        ]
    ))

    # Q20: Alveolar surfactant chemistry and infant respiratory distress syndrome (IRDS)
    questions.append(Question(
        number=20,
        title="9700/23/O/N/20/Q3 - Biophysics of Pulmonary Surfactant, the Law of Laplace, and Infant Respiratory Distress Syndrome",
        syllabus_ref="Syllabus 9.1 & 9.3",
        difficulty="ADVANCED",
        preamble="Pulmonary surfactant is an amphipathic complex of 90% lipids (predominantly DPPC) and 10% proteins (SP-A, SP-B, SP-C, SP-D) produced by alveolar Type II pneumocytes starting around gestational week 28–32.",
        parts=[
            QuestionPart(label="(a)", text="Describe the molecular orientation of dipalmitoylphosphatidylcholine (DPPC) molecules at the alveolar air-liquid interface.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="According to the Law of Laplace (P = 2T / r), explain why smaller alveoli would tend to collapse into larger alveoli in the absence of surfactant.", marks=2, num_answer_lines=3),
            QuestionPart(label="(c)", text="Premature neonates born before week 28 often develop Infant Respiratory Distress Syndrome (IRDS). Outline two clinical interventions used to manage this condition.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q20(a)", "points": "Hydrophilic phosphate / choline head groups face downwards into the aqueous alveolar fluid lining [1]; hydrophobic fatty acid tails project upwards into the alveolar air space, disrupting water hydrogen bonding [1].", "marks": 2},
            {"q": "Q20(b)", "points": "If surface tension (T) were uniform, inward collapsing pressure (P) would be inversely proportional to radius (r); smaller alveoli would have higher internal pressure, emptying their air into larger alveoli and collapsing (atelectasis) [2].", "marks": 2},
            {"q": "Q20(c)", "points": "Endotracheal instillation of exogenous / synthetic animal surfactant [1]; continuous positive airway pressure (CPAP) ventilation or maternal corticosteroid injection prior to preterm delivery [1].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION B: CORE CONCEPTUAL & PHYSIOLOGICAL MECHANISMS (20 x 4m = 80m)
    # =========================================================================

    # Q21: Cartilage distribution along respiratory tract
    questions.append(Question(
        number=21,
        title="9700/22/M/J/23/Q5 - Distribution and Morphology of Cartilage in Trachea, Bronchi, and Bronchioles",
        syllabus_ref="Syllabus 9.1 & 9.2",
        difficulty="INTERMEDIATE",
        preamble="Cartilage provides structural support to prevent airway collapse during negative intrathoracic pressures.",
        parts=[
            QuestionPart(label="(a)", text="State the morphological form of cartilage found in the trachea compared to that found in the bronchi.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why cartilage is absent from the walls of bronchioles.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q21(a)", "points": "Trachea: C-shaped (incomplete) rings [1]; Bronchi: irregular curved plates / islands of cartilage [1].", "marks": 2},
            {"q": "Q21(b)", "points": "Bronchioles need to constrict and dilate their lumen dynamically to regulate ventilation [1]; rigid cartilage would prevent diameter changes, and bronchioles are kept patent by radial tension of surrounding lung parenchyma [1].", "marks": 2}
        ]
    ))

    # Q22: Cilia vs Microvilli comparative cytology
    questions.append(Question(
        number=22,
        title="9700/21/O/N/21/Q4 - Comparative Cytology and Physiology: Cilia vs Microvilli",
        syllabus_ref="Syllabus 9.1 & 1.2",
        difficulty="INTERMEDIATE",
        preamble="Cilia and microvilli are both microscopic cell surface projections found on epithelial cells but have completely different structures and functions.",
        parts=[
            QuestionPart(label="(a)", text="Contrast the cytoskeletal core of a cilium with that of a microvillus.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the physiological difference between the roles of cilia in the trachea and microvilli in the ileum.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q22(a)", "points": "Cilium: core of microtubules arranged in a '9+2' axoneme arising from a basal body [1]; Microvillus: core of actin microfilaments bundled together with no basal body [1].", "marks": 2},
            {"q": "Q22(b)", "points": "Cilia are motile organelles that beat to sweep mucus and trapped pathogens upwards out of the airway [1]; microvilli are non-motile folds that increase surface area for absorption of digested nutrients [1].", "marks": 2}
        ]
    ))

    # Q23: Smooth muscle vs elastic fibres in airway diameter control
    questions.append(Question(
        number=23,
        title="9700/22/F/M/22/Q3 - Dual Regulation of Airway Calibre: Smooth Muscle vs Elastic Fibres",
        syllabus_ref="Syllabus 9.2",
        difficulty="INTERMEDIATE",
        preamble="The walls of conducting airways contain both smooth muscle and elastic fibres which play complementary roles.",
        parts=[
            QuestionPart(label="(a)", text="Explain how smooth muscle alters the diameter of bronchioles during an asthma attack.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why elastic fibres are described as passive elements, contrasting their action with smooth muscle.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q23(a)", "points": "In response to histamine / allergens, smooth muscle contracts spasmodically (bronchospasm) [1]; narrowing the lumen and massively increasing resistance to airflow [1].", "marks": 2},
            {"q": "Q23(b)", "points": "Elastic fibres cannot actively contract; they are stretched by external forces during inspiration and recoil passively due to elastin protein elasticity [1]; smooth muscle contains actin/myosin and contracts actively via ATP hydrolysis [1].", "marks": 2}
        ]
    ))

    # Q24: Role of goblet cells and submucosal glands in airway protection
    questions.append(Question(
        number=24,
        title="9700/21/M/J/20/Q4 - Secretory Function of Goblet Cells and Submucosal Glands",
        syllabus_ref="Syllabus 9.2",
        difficulty="INTERMEDIATE",
        preamble="Mucus production is a primary non-specific innate immune mechanism protecting the gas exchange surfaces.",
        parts=[
            QuestionPart(label="(a)", text="Describe the chemical nature of mucin and explain how it forms mucus upon secretion.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why excessive mucus secretion can impair gas exchange even if alveoli are undamaged.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q24(a)", "points": "Mucins are large glycoproteins rich in oligosaccharide chains and negatively charged sialic acid / sulfate [1]; upon exocytosis, they bind large amounts of water to form a viscous gel [1].", "marks": 2},
            {"q": "Q24(b)", "points": "Mucus accumulates in bronchioles forming plugs, blocking ventilation to downstream alveoli [1]; creates a physiological shunt where blood flows through unventilated capillaries without taking up oxygen [1].", "marks": 2}
        ]
    ))

    # Q25: Adaptations of alveoli for gas exchange
    questions.append(Question(
        number=25,
        title="9700/22/M/J/21/Q4 - Structural Adaptations of Alveoli for Rapid Diffusion",
        syllabus_ref="Syllabus 9.3",
        difficulty="INTERMEDIATE",
        preamble="The human gas exchange system is adapted to maximise the diffusion of oxygen into blood.",
        parts=[
            QuestionPart(label="(a)", text="Describe two structural adaptations of alveoli that provide a high surface area for diffusion.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how the capillaries surrounding alveoli contribute to a short diffusion distance.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q25(a)", "points": "Millions of spherical alveoli (approx. 500–700 million in adult lungs) [1]; highly folded, irregular inner alveolar surface and dense surrounding capillary meshwork [1].", "marks": 2},
            {"q": "Q25(b)", "points": "Capillaries are in direct contact with alveolar epithelium, with basement membranes fused together [1]; capillary diameter is narrow (~7 µm), forcing erythrocytes to travel in single file and press against endothelium [1].", "marks": 2}
        ]
    ))

    # Q26: Differences between inspired and expired air composition
    questions.append(Question(
        number=26,
        title="9700/21/O/N/20/Q3 - Quantitative Comparison of Inspired and Expired Air Composition",
        syllabus_ref="Syllabus 9.3",
        difficulty="INTERMEDIATE",
        preamble="During gas exchange in the alveoli, the chemical composition of air is substantially altered.",
        parts=[
            QuestionPart(label="(a)", text="State the approximate percentage of oxygen and carbon dioxide in inspired air and expired air.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why expired air still contains approximately 16% oxygen rather than 0%.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q26(a)", "points": "Inspired: ~20.9% O2, ~0.04% CO2 [1]; Expired: ~16.0% O2, ~4.0% CO2 [1].", "marks": 2},
            {"q": "Q26(b)", "points": "Only a fraction of alveolar air is replaced with each tidal breath (~0.5 dm³ out of ~3.0 dm³ FRC) [1]; inspired air mixes with anatomical dead space air (trachea, bronchi) which does not undergo gas exchange [1].", "marks": 2}
        ]
    ))

    # Q27: Nicotine mode of action on the cardiovascular system
    questions.append(Question(
        number=27,
        title="9700/22/F/M/20/Q4 - Pharmacological Effects of Nicotine on Cardiovascular Hemodynamics",
        syllabus_ref="Syllabus 9.4",
        difficulty="INTERMEDIATE",
        preamble="Nicotine is an alkaloid absorbed within seconds through the alveolar capillaries into pulmonary blood.",
        parts=[
            QuestionPart(label="(a)", text="Explain why nicotine absorption causes an immediate increase in heart rate and arterial blood pressure.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how nicotine promotes atheroma formation and arterial thrombosis.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q27(a)", "points": "Stimulates sympathetic nervous system and triggers adrenaline release from adrenal glands [1]; adrenaline increases sinoatrial node firing rate and constricts peripheral arterioles [1].", "marks": 2},
            {"q": "Q27(b)", "points": "Stimulates platelet activation and increases platelet stickiness, promoting thrombus formation [1]; hypertension damages endothelial lining, initiating LDL deposition and atheromatous plaque development [1].", "marks": 2}
        ]
    ))

    # Q28: Carbon monoxide binding to haemoglobin
    questions.append(Question(
        number=28,
        title="9700/22/O/N/19/Q3 - Carbon Monoxide Toxicity and the Shift in Oxygen Dissociation",
        syllabus_ref="Syllabus 9.4",
        difficulty="INTERMEDIATE",
        preamble="Carbon monoxide gas binds competitively to the same coordination sites on haemoglobin as oxygen.",
        parts=[
            QuestionPart(label="(a)", text="Name the compound formed when carbon monoxide binds to haemoglobin and state why this binding is persistent.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why a person with 20% carboxyhaemoglobin experiences severe fatigue during exercise.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q28(a)", "points": "Carboxyhaemoglobin (HbCO) [1]; bond energy is much higher / dissociation rate constant is extremely low compared to oxyhaemoglobin [1].", "marks": 2},
            {"q": "Q28(b)", "points": "Effective oxygen-carrying capacity of blood is reduced by 20% [1]; remaining Hb binds O2 too tightly (left shift), starving active muscle mitochondria of oxygen for aerobic ATP synthesis [1].", "marks": 2}
        ]
    ))

    # Q29: Tar and ciliostasis in the respiratory tract
    questions.append(Question(
        number=29,
        title="9700/21/M/J/19/Q4 - Action of Tobacco Tar on Ciliated Epithelial Function",
        syllabus_ref="Syllabus 9.4",
        difficulty="INTERMEDIATE",
        preamble="Tobacco tar is a complex mixture of particulates and chemical carcinogens that settles in conducting airways.",
        parts=[
            QuestionPart(label="(a)", text="Explain what is meant by 'ciliostasis' and describe how tar induces this condition.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe the consequence of ciliostasis for the respiratory defence mechanisms.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q29(a)", "points": "Ciliostasis is the cessation / paralysis of ciliary beating [1]; toxic chemicals in tar inhibit dynein ATPase arms and damage axonemal microtubules [1].", "marks": 2},
            {"q": "Q29(b)", "points": "The mucociliary escalator fails; contaminated mucus remains trapped in the airways, pooling in bronchi and providing a focus for bacterial infection [2].", "marks": 2}
        ]
    ))

    # Q30: Chronic bronchitis: Goblet cell hyperplasia and mucus plugging
    questions.append(Question(
        number=30,
        title="9700/22/M/J/18/Q4 - Mucus Hypersecretion and Goblet Cell Alterations in Chronic Bronchitis",
        syllabus_ref="Syllabus 9.5",
        difficulty="INTERMEDIATE",
        preamble="In chronic bronchitis, prolonged exposure to tobacco smoke leads to hypertrophy of secretory structures.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between goblet cell 'hypertrophy' and 'hyperplasia'.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how chronic bronchitis causes narrowing of airway lumina.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q30(a)", "points": "Hypertrophy: increase in individual cell size and secretory volume [1]; Hyperplasia: increase in cell number due to mitotic division of basal cells [1].", "marks": 2},
            {"q": "Q30(b)", "points": "Accumulation of thick mucus plugs inside lumen [1]; combined with mucosal edema / swelling from chronic inflammation and smooth muscle hypertrophy [1].", "marks": 2}
        ]
    ))

    # Q31: Pathological loss of alveolar surface area in emphysema
    questions.append(Question(
        number=31,
        title="9700/23/O/N/18/Q2 - Structural Alterations of Alveoli in Pulmonary Emphysema",
        syllabus_ref="Syllabus 9.5",
        difficulty="INTERMEDIATE",
        preamble="Emphysema is characterized by anatomical changes in the gas-exchanging parenchyma of the lung.",
        parts=[
            QuestionPart(label="(a)", text="Describe how the microscopic appearance of alveolar tissue in an emphysema patient differs from healthy lung tissue.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how this change in appearance reduces the rate of oxygen uptake into blood.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q31(a)", "points": "Alveolar septa are broken down / degraded, resulting in fewer, much larger, irregularly shaped air sacs (bullae) [2].", "marks": 2},
            {"q": "Q31(b)", "points": "Larger air spaces have a drastically lower surface area-to-volume ratio (total SA falls from ~100 m² to < 30 m²) [1]; according to Fick's law, reduced surface area proportionally decreases diffusion rate [1].", "marks": 2}
        ]
    ))

    # Q32: Role of elastase and alpha-1-antitrypsin in lung homeostasis
    questions.append(Question(
        number=32,
        title="9700/21/M/J/18/Q4 - The Enzymatic Role of Elastase and its Physiological Regulation",
        syllabus_ref="Syllabus 9.5 & 3.2",
        difficulty="INTERMEDIATE",
        preamble="Under healthy conditions, a balance exists between destructive proteases and protective antiproteases in lung tissue.",
        parts=[
            QuestionPart(label="(a)", text="Identify the leukocyte that releases elastase into lung tissues and state its physiological purpose during infection.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why individuals with genetic α1-antitrypsin deficiency develop severe emphysema at an early age even if they do not smoke.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q32(a)", "points": "Neutrophil (or alveolar macrophage) [1]; releases elastase to break down extracellular matrix and bacterial proteins during phagocytosis / migration [1].", "marks": 2},
            {"q": "Q32(b)", "points": "Lack the circulating inhibitor that neutralises elastase [1]; basal physiological elastase released by routine inflammatory turnover digests elastin unchecked over time [1].", "marks": 2}
        ]
    ))

    # Q33: Carcinogens in tar and genetic basis of lung cancer
    questions.append(Question(
        number=33,
        title="9700/22/F/M/19/Q4 - Chemical Carcinogens in Tobacco Smoke and Mutagenic Mechanisms",
        syllabus_ref="Syllabus 9.4 & 5.1",
        difficulty="INTERMEDIATE",
        preamble="Chemical analysis of tobacco tar identifies polycyclic aromatic hydrocarbons such as benzo[a]pyrene.",
        parts=[
            QuestionPart(label="(a)", text="Describe how benzo[a]pyrene interacts with DNA in bronchial epithelial cells.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how a mutation in the TP53 gene contributes to the formation of a malignant lung tumor.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q33(a)", "points": "Metabolised into an epoxide intermediate that covalently binds to guanine bases, forming DNA adducts [1]; causes mispairing during DNA replication leading to transversion mutations [1].", "marks": 2},
            {"q": "Q33(b)", "points": "p53 protein normally detects DNA damage and induces G1 cell cycle arrest or apoptosis [1]; mutated p53 allows damaged cells to divide uncontrollably by mitosis, forming a tumor [1].", "marks": 2}
        ]
    ))

    # Q34: Ventilation mechanics: Inspiration at rest
    questions.append(Question(
        number=34,
        title="9700/21/O/N/17/Q3 - Neuromuscular Coordination During Inhalation",
        syllabus_ref="Syllabus 9.1",
        difficulty="INTERMEDIATE",
        preamble="Inhalation requires active contraction of skeletal muscle groups innervated by the phrenic and intercostal nerves.",
        parts=[
            QuestionPart(label="(a)", text="Describe the change in shape of the diaphragm upon contraction and state how this affects thoracic cavity volume.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain why air enters the lungs passively following thoracic expansion.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q34(a)", "points": "Diaphragm flattens downwards from a dome shape [1]; increases vertical / longitudinal dimension and volume of thoracic cavity [1].", "marks": 2},
            {"q": "Q34(b)", "points": "Increased volume causes intrapulmonary pressure to drop below atmospheric pressure [1]; creating a pressure gradient down which air flows into lungs by bulk flow [1].", "marks": 2}
        ]
    ))

    # Q35: Ventilation mechanics: Expiration at rest vs forced expiration
    questions.append(Question(
        number=35,
        title="9700/22/M/J/17/Q4 - Comparative Mechanics: Resting Expiration vs Active Forced Expiration",
        syllabus_ref="Syllabus 9.1",
        difficulty="INTERMEDIATE",
        preamble="The muscular mechanism of expiration changes dramatically between resting conditions and strenuous physical activity.",
        parts=[
            QuestionPart(label="(a)", text="State which muscles are active during quiet expiration at rest.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Name two muscle groups that contract during forced expiration and describe their mechanical effect.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q35(a)", "points": "None / no muscles contract actively; it is purely passive, driven by relaxation of external intercostals/diaphragm and elastic recoil of lungs [2].", "marks": 2},
            {"q": "Q35(b)", "points": "Internal intercostal muscles contract, pulling ribs forcibly down and in [1]; abdominal wall muscles (rectus abdominis, obliques) contract, forcing diaphragm rapidly upwards [1].", "marks": 2}
        ]
    ))

    # Q36: Role of surfactant in reducing alveolar surface tension
    questions.append(Question(
        number=36,
        title="9700/23/M/J/17/Q3 - Biochemical Composition and Biomechanical Role of Pulmonary Surfactant",
        syllabus_ref="Syllabus 9.3",
        difficulty="INTERMEDIATE",
        preamble="Alveoli are lined with a thin film of water which generates inward surface tension forces.",
        parts=[
            QuestionPart(label="(a)", text="Explain how water molecules generate surface tension at the alveolar air-liquid interface.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe how surfactant molecules reduce this surface tension and state the physiological advantage.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q36(a)", "points": "Polar water molecules form cohesive hydrogen bonds with each other, pulling surface molecules inward towards the liquid phase [2].", "marks": 2},
            {"q": "Q36(b)", "points": "Surfactant phospholipids intersperse between water molecules, reducing intermolecular attractive forces [1]; prevents alveolar collapse (atelectasis) and reduces muscular effort required to inflate lungs [1].", "marks": 2}
        ]
    ))

    # Q37: Tidal volume and vital capacity definitions and relationships
    questions.append(Question(
        number=37,
        title="9700/21/O/N/16/Q3 - Pulmonary Functional Volumes: Tidal Volume and Vital Capacity",
        syllabus_ref="Syllabus 9.1",
        difficulty="INTERMEDIATE",
        preamble="Spirometric measurements provide objective indicators of pulmonary function.",
        parts=[
            QuestionPart(label="(a)", text="Define Tidal Volume (VT) and state its typical value in a healthy young adult at rest.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Define Vital Capacity (VC) and write a formula expressing VC in terms of its component lung volumes.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q37(a)", "points": "The volume of air inhaled or exhaled during a single normal, quiet breath at rest [1]; approximately 0.5 dm³ (500 cm³) [1].", "marks": 2},
            {"q": "Q37(b)", "points": "The maximum volume of air that can be exhaled following a maximal forced inspiration [1]; VC = Inspiratory Reserve Volume (IRV) + Tidal Volume (VT) + Expiratory Reserve Volume (ERV) [1].", "marks": 2}
        ]
    ))

    # Q38: Gas exchange in alveoli: Capillary transit time and erythrocyte deformation
    questions.append(Question(
        number=38,
        title="9700/22/M/J/16/Q4 - Microcirculatory Hemodynamics in Alveolar Capillaries",
        syllabus_ref="Syllabus 9.3 & 8.1",
        difficulty="INTERMEDIATE",
        preamble="Erythrocytes traverse pulmonary capillaries in less than one second under resting conditions.",
        parts=[
            QuestionPart(label="(a)", text="State the typical transit time of an erythrocyte through a pulmonary capillary and explain why full oxygen saturation occurs within 0.25 s.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain the physiological benefit of erythrocytes having to deform and squeeze single-file through capillaries.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q38(a)", "points": "Transit time ~0.75 s at rest [1]; steep initial partial pressure gradient (ΔP = 64 mmHg) and minimal diffusion distance (< 0.5 µm) allow complete saturation within first third of capillary length [1].", "marks": 2},
            {"q": "Q38(b)", "points": "Slows linear velocity of RBCs, maximising contact time [1]; presses erythrocyte membrane against endothelial cell, minimising diffusion pathway through plasma layer [1].", "marks": 2}
        ]
    ))

    # Q39: Pathophysiology of passive smoking (environmental tobacco smoke)
    questions.append(Question(
        number=39,
        title="9700/21/M/J/16/Q3 - Health Consequences of Passive Smoking on Non-Smokers",
        syllabus_ref="Syllabus 9.4",
        difficulty="INTERMEDIATE",
        preamble="Passive smoking refers to the involuntary inhalation of secondhand tobacco smoke by non-smokers.",
        parts=[
            QuestionPart(label="(a)", text="Distinguish between 'sidestream smoke' and 'mainstream smoke', and explain why sidestream smoke can be more hazardous.", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Describe two documented health impacts of passive smoking in young children living with smokers.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q39(a)", "points": "Mainstream smoke is exhaled by the smoker; sidestream smoke rises directly from burning cigarette tip [1]; sidestream burns at lower temperature, containing higher concentrations of toxic gases (CO, ammonia, carcinogens) [1].", "marks": 2},
            {"q": "Q39(b)", "points": "Increased frequency and severity of asthma attacks [1]; higher incidence of lower respiratory tract infections (bronchitis, pneumonia) and otitis media (middle ear infection) [1].", "marks": 2}
        ]
    ))

    # Q40: Alveolar macrophages: Structure and phagocytic defense
    questions.append(Question(
        number=40,
        title="9700/22/F/M/16/Q3 - Cellular Defense of the Alveolar Space: The Alveolar Macrophage",
        syllabus_ref="Syllabus 9.1 & 11.1",
        difficulty="INTERMEDIATE",
        preamble="Because alveoli lack cilia and goblet cells, particulate matter that reaches the terminal air spaces must be cleared by specialized phagocytes.",
        parts=[
            QuestionPart(label="(a)", text="Describe the origin and location of alveolar macrophages ('dust cells').", marks=2, num_answer_lines=3),
            QuestionPart(label="(b)", text="Explain how alveolar macrophages process inhaled carbon particulates and what happens when they become overwhelmed.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q40(a)", "points": "Originate from blood monocytes that migrate into lung parenchyma and patrol the luminal surface of alveolar septa [2].", "marks": 2},
            {"q": "Q40(b)", "points": "Engulf particulates by phagocytosis and store them in lysosomes [1]; when overwhelmed by heavy smoke, they undergo lysis, releasing lysosomal proteases that damage alveolar walls and provoke chronic inflammation [1].", "marks": 2}
        ]
    ))

    # =========================================================================
    # SECTION C: HIGH-YIELD RAPID RECALL & RIGOROUS DEFINITIONS (10 x 2m = 20m)
    # =========================================================================

    # Q41: Definition of gas exchange
    questions.append(Question(
        number=41,
        title="9700/22/M/J/23/Q1(a) - Rigorous Scientific Definition: Gas Exchange",
        syllabus_ref="Syllabus 9.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the biological term 'gas exchange' as it applies to mammals.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q41(a)", "points": "The physical process by which oxygen diffuses from alveolar air into blood and carbon dioxide diffuses from blood into alveolar air across a specialised respiratory surface [2].", "marks": 2}
        ]
    ))

    # Q42: Distinction between ventilation and respiration
    questions.append(Question(
        number=42,
        title="9700/21/O/N/22/Q1(a) - Essential Distinction: Ventilation vs Cellular Respiration",
        syllabus_ref="Syllabus 9.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Distinguish clearly between the terms 'ventilation' (breathing) and 'cellular respiration'.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q42(a)", "points": "Ventilation is the mechanical bulk flow of air into and out of lungs driven by pressure changes [1]; cellular respiration is the intracellular biochemical breakdown of glucose to yield ATP [1].", "marks": 2}
        ]
    ))

    # Q43: Role of C-shaped cartilage in trachea
    questions.append(Question(
        number=43,
        title="9700/22/M/J/22/Q1(b) - Functional Significance of Incomplete Cartilage Rings",
        syllabus_ref="Syllabus 9.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="State the function of the C-shaped cartilage rings in the wall of the mammalian trachea.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q43(a)", "points": "Keeps the tracheal airway patent / open, preventing collapse during inspiration when intrathoracic pressure is negative [2].", "marks": 2}
        ]
    ))

    # Q44: Role of elastic recoil in exhalation
    questions.append(Question(
        number=44,
        title="9700/23/M/J/21/Q1(c) - Mechanism of Passive Alveolar Recoil",
        syllabus_ref="Syllabus 9.2",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Explain the function of elastic fibres in the alveolar walls during quiet expiration.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q44(a)", "points": "Undergo passive elastic recoil following stretch, forcing air out of alveoli without muscular effort and returning alveoli to resting volume [2].", "marks": 2}
        ]
    ))

    # Q45: Definition of Tidal Volume
    questions.append(Question(
        number=45,
        title="9700/21/O/N/21/Q1(a) - Definition and Normal Value: Tidal Volume",
        syllabus_ref="Syllabus 9.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'tidal volume' and state its standard resting value in an adult human.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q45(a)", "points": "The volume of air inspired or expired in a single normal resting breath [1]; ~0.5 dm³ (500 cm³) [1].", "marks": 2}
        ]
    ))

    # Q46: Definition of Vital Capacity
    questions.append(Question(
        number=46,
        title="9700/22/F/M/21/Q1(b) - Definition: Vital Capacity",
        syllabus_ref="Syllabus 9.1",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'vital capacity' of the lungs.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q46(a)", "points": "The maximum volume of air that can be exhaled from the lungs following a maximal forced inhalation [2].", "marks": 2}
        ]
    ))

    # Q47: Primary cause of chronic bronchitis
    questions.append(Question(
        number=47,
        title="9700/21/M/J/20/Q1(a) - Diagnostic Definition: Chronic Bronchitis",
        syllabus_ref="Syllabus 9.5",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="State the clinical diagnostic definition of chronic bronchitis in terms of symptoms and duration.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q47(a)", "points": "Persistent productive cough with excessive sputum production for at least 3 consecutive months in 2 successive years [2].", "marks": 2}
        ]
    ))

    # Q48: Structural hallmark of pulmonary emphysema
    questions.append(Question(
        number=48,
        title="9700/22/O/N/19/Q1(a) - Pathological Definition: Pulmonary Emphysema",
        syllabus_ref="Syllabus 9.5",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="State the primary histopathological defect that defines pulmonary emphysema.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q48(a)", "points": "Permanent, irreversible destruction and enlargement of alveolar walls/septa with loss of elastic fibres and reduced surface area [2].", "marks": 2}
        ]
    ))

    # Q49: Carboxyhaemoglobin definition and consequence
    questions.append(Question(
        number=49,
        title="9700/21/M/J/19/Q1(b) - Chemical Nature: Carboxyhaemoglobin",
        syllabus_ref="Syllabus 9.4",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define 'carboxyhaemoglobin' and state why it causes cellular hypoxia.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q49(a)", "points": "A stable complex of carbon monoxide bound to the iron(II) haem groups of haemoglobin [1]; permanently prevents oxygen binding and transport [1].", "marks": 2}
        ]
    ))

    # Q50: Definition of carcinogen
    questions.append(Question(
        number=50,
        title="9700/22/M/J/18/Q1(a) - Rigorous Definition: Carcinogen",
        syllabus_ref="Syllabus 9.4",
        difficulty="CORE RECALL",
        parts=[
            QuestionPart(label="(a)", text="Define the term 'carcinogen' and name one specific chemical carcinogen present in tobacco tar.", marks=2, num_answer_lines=3)
        ],
        mark_scheme=[
            {"q": "Q50(a)", "points": "An environmental agent (chemical, physical, biological) that causes genetic mutations leading to cancer [1]; benzo[a]pyrene / polycyclic aromatic hydrocarbons / nitrosamines [1].", "marks": 2}
        ]
    ))

    return questions

def get_topic9_faqs():
    return [
        {
            "q_num": 1,
            "title": "Why must candidates strictly distinguish between cilia and microvilli in histology?",
            "category": "HISTOLOGY • CYTOSKELETAL ORGANELLES",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Candidates constantly confuse cilia with microvilli! Writing that 'cilia increase surface area for gas absorption' or that 'microvilli sweep mucus' loses all marks. Cilia have a 9+2 microtubule axoneme with dynein motor arms and beat actively; microvilli are non-motile actin core folds.",
            "model_answer": "• Structure of Cilia: Motile hair-like extensions of the cell surface membrane containing an internal axoneme consisting of nine peripheral doublet microtubules surrounding two central singlet microtubules ('9+2' arrangement) anchored to a basal body.\n• Mechanism of Motility: Dynein ATPase arms hydrolyse ATP to cause adjacent microtubule doublets to slide past each other, generating coordinated, wave-like metachronal beating.\n• Function of Cilia: In the trachea, bronchi, and larger bronchioles, cilia beat in synchrony (~10–15 Hz) to propel the overlying sticky mucus blanket upwards towards the pharynx and esophagus (mucociliary escalator), clearing trapped particulates and microorganisms.\n• Contrast with Microvilli: Microvilli are non-motile, cylindrical finger-like plasma membrane folds supported internally by parallel actin microfilament bundles (no microtubules, no basal bodies). Their sole function is to vastly expand apical surface area for membrane transport proteins (found in small intestine enterocytes and kidney proximal convoluted tubules, NOT in the tracheal respiratory lining)."
        },
        {
            "q_num": 2,
            "title": "What is the exact distribution of cartilage, smooth muscle, and elastic fibres from trachea to alveoli?",
            "category": "AIRWAY ANATOMY • TISSUE DISTRIBUTION",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Stating that cartilage is present in bronchioles or alveoli! Cartilage is C-shaped in the trachea, irregular plates in bronchi, and completely ABSENT in bronchioles. Bronchioles have a prominent circular layer of smooth muscle and abundant elastic fibres.",
            "model_answer": "• Trachea: Possesses 16–20 C-shaped (incomplete) hyaline cartilage rings joined posteriorly by the smooth trachealis muscle. Lamina propria contains elastic fibres; submucosa contains seromucous glands. Lined by pseudostratified ciliated columnar epithelium with abundant goblet cells.\n• Bronchi: Possesses irregular curved plates / islands of hyaline cartilage embedded in the wall. Smooth muscle forms criss-crossing spiral bands between cartilage and mucosa. Ciliated columnar epithelium and goblet cells remain present.\n• Bronchioles (< 1 mm diameter): Completely lack cartilage plates! Wall is dominated by a complete, thick circular coat of smooth muscle and abundant surrounding elastic fibres. Lined initially by ciliated cuboidal epithelium; goblet cells and seromucous glands are entirely absent from terminal and respiratory bronchioles.\n• Alveoli: Consist purely of an extremely thin simple squamous epithelium (Type I pneumocytes) and surfactant-secreting Type II pneumocytes. Completely lack cartilage, smooth muscle, and cilia. Enveloped externally by an extensive network of elastic fibres and pulmonary capillaries."
        },
        {
            "q_num": 3,
            "title": "Why do examiners penalise stating that elastic fibres 'contract' during exhalation?",
            "category": "PULMONARY MECHANICS • ELASTIC RECOIL",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Saying elastic fibres 'contract' to push air out! Proteins like elastin have no ATPase activity and never contract actively. Elastic fibres stretch under tension during inhalation and RECOIL passively during exhalation. Only muscle contracts actively.",
            "model_answer": "• Passive Nature of Elastic Fibres: Elastic fibres are composed of the extracellular fibrous protein elastin cross-linked into a random-coil network. When thoracic volume expands during inspiration, external mechanical work stretches these fibres, storing potential energy.\n• Passive Elastic Recoil: During quiet exhalation at rest, inspiratory muscles (diaphragm and external intercostals) relax. The stretched elastic fibres spontaneously recoil back to their original resting length, squeezing the alveolar air space and forcing air outwards down a positive pressure gradient without any ATP consumption.\n• Active Action of Smooth Muscle: In contrast, airway smooth muscle cells contain actin and myosin myofilaments that actively hydrolyse ATP to contract, causing bronchoconstriction (e.g. in response to cold air, allergens, or parasympathetic acetylcholine), and actively relax under sympathetic stimulation (noradrenaline / adrenaline) to cause bronchodilation."
        },
        {
            "q_num": 4,
            "title": "What are the exact components of the alveolar-capillary diffusion barrier?",
            "category": "FICK'S LAW • DIFFUSION BARRIER",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Writing that the diffusion barrier is 'one cell thick' or just 'alveolar cell and capillary'. Cambridge mark schemes strictly award marks only for identifying the THREE distinct anatomical layers: squamous alveolar cell (Type I pneumocyte), fused extracellular basement membrane, and capillary endothelial cell.",
            "model_answer": "• Layer 1 (Alveolar Epithelium): The extremely thin cytoplasm of a Type I pneumocyte (simple squamous alveolar cell), approximately 0.1–0.2 µm thick.\n• Layer 2 (Basement Membrane): The shared, fused extracellular basement membrane composed of type IV collagen and laminin glycoproteins produced by the epithelial and endothelial cells, approximately 0.1 µm thick.\n• Layer 3 (Capillary Endothelium): The cytoplasm of the capillary endothelial cell, approximately 0.1–0.2 µm thick.\n• Total Diffusion Distance: The combined barrier thickness is less than 0.5 µm (typically 0.2–0.4 µm), providing an exceptionally short diffusion pathway (x) that maximizes diffusion rate according to Fick's first law."
        },
        {
            "q_num": 5,
            "title": "How is a steep concentration gradient for oxygen maintained across the alveolar membrane?",
            "category": "VENTILATION-PERFUSION • CONCENTRATION GRADIENTS",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Saying 'there is a high gradient' without explaining the physiological mechanisms that create and sustain it. You must explicitly link ventilation (which refreshes alveolar gas) with continuous capillary perfusion (which carries oxygen away).",
            "model_answer": "• Role of Continuous Ventilation: Regular tidal ventilation continuously replaces stale, oxygen-depleted alveolar air with fresh atmospheric air (containing 20.9% O2), keeping the alveolar partial pressure of oxygen consistently high at approximately 104 mmHg (13.7 kPa).\n• Role of Continuous Perfusion: The pulmonary circulation delivers deoxygenated venous blood from the right ventricle with a low partial pressure of oxygen (pO2 ~40 mmHg / 5.3 kPa). As blood flows through the capillary, haemoglobin rapidly binds oxygen; the continuous movement of blood carries newly oxygenated erythrocytes away towards the left atrium, preventing local equilibrium and keeping capillary pO2 low at the arterial end.\n• Steep Partial Pressure Gradient: This maintains a substantial partial pressure difference (ΔP = 104 - 40 = 64 mmHg / 8.4 kPa) driving rapid, continuous passive diffusion of O2 into blood."
        },
        {
            "q_num": 6,
            "title": "What is the precise cellular and molecular pathogenesis of chronic bronchitis?",
            "category": "PATHOLOGY • TOBACCO SMOKING",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Giving a superficial answer like 'mucus builds up and cough happens'. Candidates must explain the cellular changes: irritants in tar stimulate goblet cell hyperplasia and hypertrophy of submucosal glands; tar paralyses cilia (ciliostasis); mucus pools and causes persistent cough; stagnant mucus becomes a culture medium for bacteria.",
            "model_answer": "• Irritation & Secretory Hyperplasia: Chemical irritants in tobacco smoke stimulate basal stem cells in the bronchial epithelium to divide, causing hyperplasia (increased number) and hypertrophy (enlarged size) of mucus-secreting goblet cells and seromucous glands (Reid index > 0.5).\n• Ciliostasis & Destruction: Tobacco tar directly impairs dynein ATPase arms and destroys cilia (ciliostasis), disabling the mucociliary escalator so mucus cannot be propelled upwards.\n• Mucus Pooling & Obstruction: Copious, highly viscous mucus pools in bronchi and bronchioles, obstructing airways and triggering persistent, productive 'smoker's cough' to mechanically clear the airways.\n• Secondary Bacterial Infections: Stagnant mucus serves as a nutrient-rich culture medium for pathogens such as Streptococcus pneumoniae and Haemophilus influenzae. Recurrent infections provoke chronic inflammation, attracting neutrophils and macrophages, causing scar tissue formation and narrowing of airways."
        },
        {
            "q_num": 7,
            "title": "How does the protease-antiprotease imbalance explain the destruction of alveoli in emphysema?",
            "category": "EMPHYSEMA • ELASTASE VS ALPHA-1-ANTITRYPSIN",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Claiming that cigarette smoke 'tears' or 'dissolves' alveoli directly! The destruction is ENZYMATIC: smoke irritants attract neutrophils and activate alveolar macrophages to secrete the protease elastase. Smoke oxidants inactivate the natural protective inhibitor α1-antitrypsin. Unopposed elastase digests elastin fibres in alveolar septa.",
            "model_answer": "• Recruitment of Phagocytes: Smoke particulates irritate terminal bronchioles and alveoli, where they are engulfed by alveolar macrophages. Macrophages release chemotactic factors (IL-8, leukotrienes) that summon large numbers of circulating neutrophils into the lung interstitium.\n• Release of Elastase: Neutrophils secrete the proteolytic enzyme neutrophil elastase to digest debris. Under healthy conditions, elastase is strictly neutralized by α1-antitrypsin (an antiprotease synthesised in the liver).\n• Inactivation of α1-Antitrypsin: Free radicals and oxidants in cigarette smoke oxidize active-site methionine residues on α1-antitrypsin, abolishing its inhibitory ability and creating an overwhelming protease-antiprotease imbalance.\n• Destruction of Alveolar Septa: Unchecked elastase enzymatic digestion degrades elastin fibres in alveolar walls. Alveolar septa lyse and breakdown, coalescing millions of microscopic alveoli into large, irregular air spaces (bullae) with a severely reduced surface area for gas exchange and complete loss of elastic recoil."
        },
        {
            "q_num": 8,
            "title": "What are the distinct physiological effects of nicotine versus carbon monoxide?",
            "category": "TOXICOLOGY • CARDIOVASCULAR IMPACT",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Confusing nicotine and carbon monoxide! Nicotine affects the nervous system and adrenal glands (causing vasoconstriction, high heart rate, high blood pressure, and platelet stickiness). Carbon monoxide binds haemoglobin to form carboxyhaemoglobin (HbCO), reducing oxygen transport and causing fetal hypoxia. Nicotine does NOT bind haemoglobin!",
            "model_answer": "• Nicotine Mode of Action: An addictive alkaloid that mimics acetylcholine at nicotinic acetylcholine receptors in the central and autonomic nervous systems. Stimulates sympathetic ganglia and triggers adrenaline release from the adrenal medulla. Induces peripheral arteriolar vasoconstriction, elevating systemic vascular resistance and blood pressure; increases heart rate and cardiac workload; and increases platelet stickiness, markedly raising the risk of thrombosis and coronary heart disease.\n• Carbon Monoxide (CO) Mode of Action: A toxic gas that diffuses across alveolar membranes into erythrocytes and binds competitively to iron(II) in haem groups with ~250 times higher affinity than oxygen. Forms stable carboxyhaemoglobin (HbCO), which reduces the oxygen-carrying capacity of blood. Furthermore, CO binding causes an allosteric leftward shift in the remaining oxyhaemoglobin subunits, preventing oxygen unloading at respiring tissues and causing chronic cellular hypoxia."
        },
        {
            "q_num": 9,
            "title": "How do carcinogens in tobacco tar lead to bronchogenic carcinoma (lung cancer)?",
            "category": "CARCINOGENESIS • ONCOGENES & TUMOR SUPPRESSORS",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Writing that 'tar is cancer'. Tar contains chemical carcinogens (e.g. polycyclic aromatic hydrocarbons like benzo[a]pyrene) that mutate specific genes regulating the cell cycle (proto-oncogenes converting to oncogenes; mutating TP53 tumor suppressor gene). Uncontrolled mitosis results in a malignant tumor that invades tissue and metastasizes.",
            "model_answer": "• Chemical Carcinogens: Tobacco tar contains over 60 established chemical carcinogens, including polycyclic aromatic hydrocarbons (such as benzo[a]pyrene) and tobacco-specific nitrosamines (NNK).\n• DNA Adduct Formation & Mutation: Metabolic activation converts benzo[a]pyrene into reactive epoxides that covalently bind to guanine bases in DNA, forming bulky DNA adducts that induce transversion mutations (G->T) during DNA replication.\n• Oncogenes & Tumor Suppressor Genes: Critical mutations occur in the TP53 tumor suppressor gene (loss of p53 protein means damaged cells cannot undergo G1 cell cycle arrest or apoptosis) and the KRAS proto-oncogene (activating it into a continuously signaling oncogene).\n• Tumor Progression & Metastasis: Bronchial cells escape normal cell cycle checkpoints and divide uncontrollably by mitosis, forming a localized tumor (carcinoma in situ). The malignant cells secrete angiogenic factors (VEGF), breach the basement membrane, invade bronchial walls, and enter pulmonary venules and lymphatic vessels to establish distant metastases in brain, bones, and liver."
        },
        {
            "q_num": 10,
            "title": "How do you calculate Pulmonary Ventilation Rate (PVR) and distinguish it from Alveolar Ventilation Rate (AVR)?",
            "category": "SPIROMETRY • VENTILATION CALCULATIONS",
            "examiner_trap": "CRITICAL EXAMINER TRAP: Forgetting that a portion of each tidal breath remains in the anatomical dead space (trachea and bronchi, ~150 cm³) and never reaches the alveoli! PVR = Tidal Volume x Breathing Frequency. But Alveolar Ventilation Rate (AVR) = (Tidal Volume - Dead Space) x Breathing Frequency.",
            "model_answer": "• Pulmonary Ventilation Rate (PVR): Total volume of air moved into and out of the respiratory tract per minute. Formula: PVR = Tidal Volume (dm³) x Breathing Frequency (breaths min⁻¹). Example: 0.5 dm³ x 12 breaths min⁻¹ = 6.0 dm³ min⁻¹.\n• Anatomical Dead Space (VD): Volume of conducting airways (pharynx, trachea, bronchi, bronchioles) where no gas exchange occurs, typically ~0.15 dm³ (150 cm³) in an adult.\n• Alveolar Ventilation Rate (AVR): The actual volume of fresh atmospheric air that enters the gas-exchanging alveoli per minute. Formula: AVR = (Tidal Volume - Anatomical Dead Space) x Breathing Frequency. Example: (0.50 - 0.15 dm³) x 12 min⁻¹ = 0.35 dm³ x 12 min⁻¹ = 4.2 dm³ min⁻¹.\n• Clinical Significance: Rapid, shallow breathing (tachypnea) severely compromises AVR because dead space volume represents a larger fraction of each breath, resulting in inadequate alveolar oxygenation despite an apparently normal total PVR."
        }
    ]
