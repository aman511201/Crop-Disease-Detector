"""
Agricultural Disease Knowledge Base
Detailed symptoms, causal agents, organic & chemical treatments,
and preventive measures for 38 crop disease classes.
"""

DISEASE_CLASSES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

DISEASE_DETAILS = {
    "Apple___Apple_scab": {
        "crop": "Apple",
        "disease": "Apple Scab",
        "scientific_name": "Venturia inaequalis",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "Moderate to High",
        "symptoms": "Olive-green to dull brown velvety spots on leaves, becoming cracked and scabby on fruit. Leaves often turn yellow and drop prematurely.",
        "causes": "High humidity, prolonged leaf wetness, and cool spring temperatures (12°C–24°C).",
        "organic_treatment": [
            "Apply liquid copper or sulfur sprays at bud break.",
            "Spray with neem oil or potassium bicarbonate solution.",
            "Rake and burn or compost fallen leaves in autumn to eliminate overwintering spores."
        ],
        "chemical_treatment": [
            "Fungicides containing Myclobutanil, Mancozeb, or Captan.",
            "Apply proactively before rain events in early spring."
        ],
        "prevention": [
            "Plant scab-resistant apple cultivars (e.g., Liberty, Freedom, Honeycrisp).",
            "Prune canopy regularly to increase sunlight penetration and accelerate leaf drying.",
            "Avoid overhead irrigation."
        ]
    },
    "Apple___Black_rot": {
        "crop": "Apple",
        "disease": "Black Rot (Frogeye Leaf Spot)",
        "scientific_name": "Botryosphaeria obtusa",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "High",
        "symptoms": "Purple flecks expanding into circular lesions with light brown centers ('frogeye' spots). Apples develop firm, concentric brown/black rot rings.",
        "causes": "Warm, humid conditions (20°C–27°C); spores survive in dead wood, mummified fruits, and bark cankers.",
        "organic_treatment": [
            "Prune out dead shoots, twigs, and branch cankers 6-8 inches below visible damage.",
            "Remove and destroy all mummified apples clinging to branches.",
            "Apply bio-fungicides like Bacillus subtilis."
        ],
        "chemical_treatment": [
            "Fungicides based on Captan, Thiophanate-methyl, or Mancozeb applied from tight cluster through harvest."
        ],
        "prevention": [
            "Maintain strict orchard sanitation; never leave infected debris under trees.",
            "Protect trees from winter injury and wood borer insects.",
            "Ensure proper drainage and air flow."
        ]
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "disease": "Cedar Apple Rust",
        "scientific_name": "Gymnosporangium juniperi-virginianae",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "Moderate",
        "symptoms": "Bright yellow-orange or reddish-orange circular spots on leaf upper surfaces. Later, small tube-like structures form on the leaf underside.",
        "causes": "Requires Eastern red cedar or juniper trees nearby to complete its dual-host life cycle; wind-blown spores during rainy spring periods.",
        "organic_treatment": [
            "Apply sulfur or copper soap sprays early when cedar galls swell in spring.",
            "Manually remove cedar galls from nearby juniper trees if feasible."
        ],
        "chemical_treatment": [
            "Myclobutanil (Immunox) or Propiconazole applied between pink bud stage and petal fall."
        ],
        "prevention": [
            "Remove ornamental or wild juniper trees within a 1-2 mile radius if possible.",
            "Select resistant cultivars such as Enterprise, Liberty, or William's Pride."
        ]
    },
    "Apple___healthy": {
        "crop": "Apple",
        "disease": "Healthy Plant",
        "scientific_name": "Malus domestica",
        "pathogen_type": "None",
        "is_healthy": True,
        "severity": "None",
        "symptoms": "Leaves are vibrant green, intact, without spots, lesions, discoloration, or curling.",
        "causes": "Optimal nutrition, clean canopy, good airflow, and effective pest management.",
        "organic_treatment": [
            "No chemical or therapeutic treatment required.",
            "Maintain balanced compost and organic mulch around the drip line."
        ],
        "chemical_treatment": [
            "None needed."
        ],
        "prevention": [
            "Continue periodic scouting every 7-10 days.",
            "Provide balanced N-P-K fertilization and adequate irrigation."
        ]
    },
    "Blueberry___healthy": {
        "crop": "Blueberry",
        "disease": "Healthy Plant",
        "scientific_name": "Vaccinium corymbosum",
        "pathogen_type": "None",
        "is_healthy": True,
        "severity": "None",
        "symptoms": "Healthy, uniform green leaves with smooth margins and no signs of chlorosis, rust, or blight.",
        "causes": "Balanced acidic soil (pH 4.5–5.5) and good drainage.",
        "organic_treatment": [
            "No treatment needed."
        ],
        "chemical_treatment": [
            "None needed."
        ],
        "prevention": [
            "Maintain soil pH at 4.5 to 5.2 with elemental sulfur.",
            "Mulch with pine needles or acidic bark chips."
        ]
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "crop": "Cherry",
        "disease": "Powdery Mildew",
        "scientific_name": "Podosphaera clandestina",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "Moderate",
        "symptoms": "White, talcum powder-like fungal patches on leaf surfaces, young shoots, and stems; leaves may curl upward and distort.",
        "causes": "High relative humidity with warm temperatures and shaded, crowded canopies.",
        "organic_treatment": [
            "Spray with potassium bicarbonate (0.5% solution) or neem oil.",
            "Apply sulfur dust or wettable sulfur (do not use above 30°C).",
            "Diluted milk spray (1:9 ratio with water) has demonstrated bio-fungicidal activity."
        ],
        "chemical_treatment": [
            "Triazole fungicides (e.g., Myclobutanil) or strobilurins (e.g., Pyraclostrobin)."
        ],
        "prevention": [
            "Prune dense branches to promote sunlight and wind penetration.",
            "Water roots directly, avoiding wetting foliage."
        ]
    },
    "Cherry_(including_sour)___healthy": {
        "crop": "Cherry",
        "disease": "Healthy Plant",
        "scientific_name": "Prunus cerasus / avium",
        "pathogen_type": "None",
        "is_healthy": True,
        "severity": "None",
        "symptoms": "Deep green foliage, robust growth, absence of leaf spotting, curling, or fungal growth.",
        "causes": "Optimal orchard care, timely pruning, balanced nutrition.",
        "organic_treatment": [
            "No treatment necessary."
        ],
        "chemical_treatment": [
            "None required."
        ],
        "prevention": [
            "Annual dormant oil spray in late winter to suppress scale and mites."
        ]
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn (Maize)",
        "disease": "Gray Leaf Spot (Cercospora)",
        "scientific_name": "Cercospora zeae-maydis",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "High",
        "symptoms": "Tan to gray rectangular lesions bounded strictly by leaf veins. Lesions merge to cause broad leaf blighting and lodging.",
        "causes": "Extended periods of high humidity (>90%) and warm temperatures (24°C–32°C); continuous corn cropping.",
        "organic_treatment": [
            "Deep tillage to bury crop residues harboring fungus.",
            "Rotate crops for at least 2 years with non-host crops like soybeans."
        ],
        "chemical_treatment": [
            "Apply foliar fungicides such as Azoxystrobin, Pyraclostrobin, or Propiconazole at tassel stage (VT to R1)."
        ],
        "prevention": [
            "Plant resistant corn hybrids.",
            "Avoid excessive plant densities that limit airflow.",
            "Ensure balanced potassium fertilization."
        ]
    },
    "Corn_(maize)___Common_rust_": {
        "crop": "Corn (Maize)",
        "disease": "Common Rust",
        "scientific_name": "Puccinia sorghi",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "Moderate",
        "symptoms": "Golden-brown to cinnamon-brown powdery pustules scattered over both leaf surfaces. Pustules rupture the epidermis.",
        "causes": "Cool to moderate temperatures (16°C–25°C) with high humidity; windborne fungal urediniospores.",
        "organic_treatment": [
            "Foliar spray of sulfur or bio-fungicide Bacillus subtilis upon early symptom detection.",
            "Crop residue management."
        ],
        "chemical_treatment": [
            "Strobilurin or triazole fungicides (Azoxystrobin + Difenoconazole) if pustules reach upper leaves early in grain fill."
        ],
        "prevention": [
            "Plant rust-tolerant or resistant corn hybrids.",
            "Early planting to avoid mid-summer spore influx."
        ]
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn (Maize)",
        "disease": "Northern Corn Leaf Blight",
        "scientific_name": "Exserohilum turcicum",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "High",
        "symptoms": "Long, elliptical cigar-shaped grayish-green to tan lesions (1 to 6 inches long) progressing from lower to upper leaves.",
        "causes": "Moderate temperatures (18°C–27°C) and extended dew periods (6-18 hours).",
        "organic_treatment": [
            "Crop debris incorporation through post-harvest conservation tillage.",
            "Trichoderma harzianum bio-agent application."
        ],
        "chemical_treatment": [
            "Foliar fungicides: Pyraclostrobin + Fluxapyroxad or Azoxystrobin + Propiconazole."
        ],
        "prevention": [
            "Choose NCLB-resistant seed hybrids containing Ht genes.",
            "Implement a 2-year crop rotation with non-grasses."
        ]
    },
    "Corn_(maize)___healthy": {
        "crop": "Corn (Maize)",
        "disease": "Healthy Plant",
        "scientific_name": "Zea mays",
        "pathogen_type": "None",
        "is_healthy": True,
        "severity": "None",
        "symptoms": "Broad, deep green leaves with clear veins and sturdy stalks without lesions or chlorotic streaks.",
        "causes": "Adequate nitrogen, optimum moisture, clean seed bed.",
        "organic_treatment": [
            "No treatment needed."
        ],
        "chemical_treatment": [
            "None."
        ],
        "prevention": [
            "Maintain side-dress nitrogen schedule and weed control."
        ]
    },
    "Grape___Black_rot": {
        "crop": "Grape",
        "disease": "Black Rot",
        "scientific_name": "Guignardia bidwellii",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "High",
        "symptoms": "Circular reddish-brown spots with dark borders and tiny black fruiting bodies on leaves; berries shrivel into hard black mummies.",
        "causes": "Warm, wet weather during early shoot and berry development.",
        "organic_treatment": [
            "Prune infected canes and remove all mummified grape clusters from vines and ground.",
            "Apply copper sulfate or lime-sulfur during early spring dormancy."
        ],
        "chemical_treatment": [
            "Mancozeb, Captan, or Tebuconazole starting at 1-3 inch shoot growth and repeating every 10-14 days until veraison."
        ],
        "prevention": [
            "Prune vines to open canopy structure ensuring rapid drying.",
            "Cultivate beneath vines to bury overwintering leaves."
        ]
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "disease": "Esca (Black Measles)",
        "scientific_name": "Phaeomoniella chlamydospora & Fomitiporia mediterranea",
        "pathogen_type": "Fungus Complex",
        "is_healthy": False,
        "severity": "Severe / Chronic",
        "symptoms": "Leaves exhibit 'tiger-stripe' interveinal chlorosis and necrosis. Berries develop dark spots resembling measles, crack and wilt.",
        "causes": "Trunk wounding, infected propagation wood, wood-decay fungal infection of xylem.",
        "organic_treatment": [
            "Mark symptomatic vines and prune last during winter.",
            "Paint fresh pruning cuts with wound sealants or Trichoderma-based protectants."
        ],
        "chemical_treatment": [
            "No curative systemic chemical; apply Thiophanate-methyl pruning wound sealants immediately after cutting."
        ],
        "prevention": [
            "Use certified disease-free nursery stock.",
            "Avoid making large pruning wounds in wet weather."
        ]
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "disease": "Leaf Blight (Isariopsis)",
        "scientific_name": "Pseudocercospora vitis",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "Moderate",
        "symptoms": "Irregular dark brown or black angular leaf spots surrounded by a faint yellowish halo; leaves turn yellow and drop prematurely.",
        "causes": "Warm, humid climates with frequent rain late in the growing season.",
        "organic_treatment": [
            "Copper hydroxide or Bordeaux mixture spray after harvest.",
            "Clear fallen foliage."
        ],
        "chemical_treatment": [
            "Fungicides containing Mancozeb, Copper Oxychloride, or Difenoconazole."
        ],
        "prevention": [
            "Improve vineyard canopy aeration.",
            "Avoid late overhead watering."
        ]
    },
    "Grape___healthy": {
        "crop": "Grape",
        "disease": "Healthy Plant",
        "scientific_name": "Vitis vinifera",
        "pathogen_type": "None",
        "is_healthy": True,
        "severity": "None",
        "symptoms": "Lush green lobed foliage, clear veins, vigorous tendril growth, no spots or powdery residues.",
        "causes": "Balanced canopy management, adequate sunshine, well-timed pruning.",
        "organic_treatment": [
            "No treatment needed."
        ],
        "chemical_treatment": [
            "None needed."
        ],
        "prevention": [
            "Maintain annual canopy management, shoot thinning, and leaf pulling."
        ]
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Orange / Citrus",
        "disease": "Citrus Greening (Huanglongbing)",
        "scientific_name": "Candidatus Liberibacter asiaticus",
        "pathogen_type": "Bacterium (Vector: Asian Citrus Psyllid)",
        "is_healthy": False,
        "severity": "Critical",
        "symptoms": "Asymmetrical blotchy mottle on leaves, yellow shoots, vein corking, small lopsided bitter fruits that remain green at bottom.",
        "causes": "Bacterium transmitted by the Asian Citrus Psyllid (Diaphorina citri) insect vector.",
        "organic_treatment": [
            "Intensive biological control of psyllids using parasitic wasps (Tamarixia radiata).",
            "Immediate eradication and burning of severely infected trees to protect surrounding grove.",
            "Nutritional foliar sprays (zinc, manganese, micronutrients) to prolong tree productivity."
        ],
        "chemical_treatment": [
            "Insecticides targeting the psyllid vector: Imidacloprid, Thiamethoxam, or Cyantraniliprole."
        ],
        "prevention": [
            "Plant only certified pathogen-free nursery trees.",
            "Install insect netting in nursery and young grove plantings."
        ]
    },
    "Peach___Bacterial_spot": {
        "crop": "Peach",
        "disease": "Bacterial Spot",
        "scientific_name": "Xanthomonas arboricola pv. pruni",
        "pathogen_type": "Bacterium",
        "is_healthy": False,
        "severity": "Moderate to High",
        "symptoms": "Angular, water-soaked purple-brown lesions on leaves that drop out, creating a 'shot-hole' appearance. Pitted fruit with gummy exudates.",
        "causes": "Warm, wet, windy weather; sandy soils with blowing abrasive sand.",
        "organic_treatment": [
            "Low-dose fixed copper sprays from dormant stage until bloom.",
            "Foliar sprays of Bacillus amyloliquefaciens."
        ],
        "chemical_treatment": [
            "Oxytetracycline (Mycoshield) sprays during the growing season when copper risks phytotoxicity."
        ],
        "prevention": [
            "Choose resistant peach cultivars (e.g., Candor, Dixired, Harvester).",
            "Avoid excessive nitrogen fertilization which causes overly succulent susceptible foliage."
        ]
    },
    "Peach___healthy": {
        "crop": "Peach",
        "disease": "Healthy Plant",
        "scientific_name": "Prunus persica",
        "pathogen_type": "None",
        "is_healthy": True,
        "severity": "None",
        "symptoms": "Glossy lanceolate green leaves without holes, yellowing, or gum spots.",
        "causes": "Good orchard drainage, balanced stone fruit nutrition.",
        "organic_treatment": [
            "No treatment needed."
        ],
        "chemical_treatment": [
            "None needed."
        ],
        "prevention": [
            "Regular dormant copper spray to prevent peach leaf curl."
        ]
    },
    "Pepper,_bell___Bacterial_spot": {
        "crop": "Bell Pepper",
        "disease": "Bacterial Spot",
        "scientific_name": "Xanthomonas euvesicatoria",
        "pathogen_type": "Bacterium",
        "is_healthy": False,
        "severity": "High",
        "symptoms": "Small, water-soaked, irregular blister-like spots on leaves that turn brown with yellow halos. Severe defoliation causes fruit sunscald.",
        "causes": "Splashing rain, overhead irrigation, temperatures between 24°C–30°C.",
        "organic_treatment": [
            "Copper bactericides mixed with Bacillus subtilis or bacteriophages.",
            "Remove and destroy severely infected pepper plants.",
            "Disinfect stakes and pruning tools with 10% bleach."
        ],
        "chemical_treatment": [
            "Copper hydroxide combined with Mancozeb (provides synergized bacterial control)."
        ],
        "prevention": [
            "Use certified disease-free hot-water-treated seed.",
            "Rotate out of solanaceous crops for minimum 2 years.",
            "Use drip irrigation under plastic mulch."
        ]
    },
    "Pepper,_bell___healthy": {
        "crop": "Bell Pepper",
        "disease": "Healthy Plant",
        "scientific_name": "Capsicum annuum",
        "pathogen_type": "None",
        "is_healthy": True,
        "severity": "None",
        "symptoms": "Dark green, smooth leaves, vigorous apical growth, flowers and developing peppers unblemished.",
        "causes": "Balanced calcium and magnesium levels, consistent watering, pest exclusion.",
        "organic_treatment": [
            "No treatment needed."
        ],
        "chemical_treatment": [
            "None needed."
        ],
        "prevention": [
            "Ensure steady calcium to avoid blossom end rot; mulch to maintain moisture."
        ]
    },
    "Potato___Early_blight": {
        "crop": "Potato",
        "disease": "Early Blight",
        "scientific_name": "Alternaria solani",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "Moderate to High",
        "symptoms": "Circular brown to dark spots on older leaves displaying distinctive concentric rings ('target-board' pattern) with yellow chlorotic halos.",
        "causes": "Warm temperatures (24°C–29°C) with alternating wet and dry cycles; nutrient-stressed plants.",
        "organic_treatment": [
            "Copper octanoate or copper sulfate foliar sprays.",
            "Neem oil and potassium bicarbonate.",
            "Prune infected lower foliage touching the soil."
        ],
        "chemical_treatment": [
            "Chlorothalonil, Mancozeb, Azoxystrobin, or Difenoconazole."
        ],
        "prevention": [
            "Maintain adequate nitrogen and potassium throughout tuber bulking.",
            "Practice 3-year crop rotation.",
            "Avoid sprinkler irrigation; water at soil level early morning."
        ]
    },
    "Potato___Late_blight": {
        "crop": "Potato",
        "disease": "Late Blight",
        "scientific_name": "Phytophthora infestans",
        "pathogen_type": "Oomycete (Water Mold)",
        "is_healthy": False,
        "severity": "Critical",
        "symptoms": "Large, irregular water-soaked dark brown to purplish-black lesions that spread rapidly. In humid conditions, white fluffy mold appears on leaf undersides. Stems turn black.",
        "causes": "Cool, humid weather (15°C–20°C, RH > 90%). Infamous cause of the Irish Potato Famine.",
        "organic_treatment": [
            "Aggressive copper hydroxide / copper sulfate sprays before rain events.",
            "Promptly rogue out and destroy infected vines to halt spore clouds.",
            "Do not compost infected plants."
        ],
        "chemical_treatment": [
            "Systemic fungicides: Metalaxyl / Mefenoxam, Cymoxanil, Propamocarb, or Mandipropamid."
        ],
        "prevention": [
            "Plant certified late-blight-free seed potatoes.",
            "Eliminate cull piles and volunteer potato plants.",
            "Hill potatoes deeply to protect tubers from spores washed through soil."
        ]
    },
    "Potato___healthy": {
        "crop": "Potato",
        "disease": "Healthy Plant",
        "scientific_name": "Solanum tuberosum",
        "pathogen_type": "None",
        "is_healthy": True,
        "severity": "None",
        "symptoms": "Robust lush foliage, rich green leaves, uniform growth with no blight spots or wilting.",
        "causes": "Certified clean tubers, cool root zone, proper hilling.",
        "organic_treatment": [
            "No treatment needed."
        ],
        "chemical_treatment": [
            "None needed."
        ],
        "prevention": [
            "Monitor foliage after rain events; hill soil regularly around stems."
        ]
    },
    "Raspberry___healthy": {
        "crop": "Raspberry",
        "disease": "Healthy Plant",
        "scientific_name": "Rubus idaeus",
        "pathogen_type": "None",
        "is_healthy": True,
        "severity": "None",
        "symptoms": "Vibrant serrated leaves, bright green canes, clean margins free of spur blight or rust.",
        "causes": "Good trellis support, well-drained loamy soil, good air circulation.",
        "organic_treatment": [
            "No treatment needed."
        ],
        "chemical_treatment": [
            "None needed."
        ],
        "prevention": [
            "Prune out floricanes after fruiting; mulch to prevent soil splashing."
        ]
    },
    "Soybean___healthy": {
        "crop": "Soybean",
        "disease": "Healthy Plant",
        "scientific_name": "Glycine max",
        "pathogen_type": "None",
        "is_healthy": True,
        "severity": "None",
        "symptoms": "Trifoliate leaves are uniformly green, free from rust pustules, target spots, or mosaic patterns.",
        "causes": "Effective rhizobium nodulation, clean seed, timely weed management.",
        "organic_treatment": [
            "No treatment needed."
        ],
        "chemical_treatment": [
            "None needed."
        ],
        "prevention": [
            "Maintain crop rotation with corn/grasses; scout for stink bugs and aphids."
        ]
    },
    "Squash___Powdery_mildew": {
        "crop": "Squash",
        "disease": "Powdery Mildew",
        "scientific_name": "Podosphaera xanthii",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "Moderate",
        "symptoms": "Talcum powder-like white spots appearing first on crown leaves and lower surfaces, spreading to cover entire leaf blade. Leaves turn yellow, brown, and brittle.",
        "causes": "Dense plant foliage, moderate temperatures (20°C–27°C), low light and high humidity.",
        "organic_treatment": [
            "Spray with potassium bicarbonate or baking soda (1 tbsp + 1 tsp horticultural oil per gallon).",
            "Neem oil or sulfur sprays at first appearance.",
            "Diluted milk whey spray (40% milk, 60% water)."
        ],
        "chemical_treatment": [
            "Trifloxystrobin, Myclobutanil, or Quinoxyfen."
        ],
        "prevention": [
            "Plant resistant squash cultivars.",
            "Space plants generously (4-6 feet) to provide air movement.",
            "Water at the base with drip hoses."
        ]
    },
    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry",
        "disease": "Leaf Scorch",
        "scientific_name": "Diplocarpon earlianum",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "Moderate",
        "symptoms": "Irregular purple or purplish-red blotches (without white centers) on upper leaf surfaces. As spots enlarge, entire leaf looks burned or scorched.",
        "causes": "Frequent rainfall and overhead irrigation; temperatures of 20°C–25°C.",
        "organic_treatment": [
            "Prune infected old leaves during post-harvest renovation.",
            "Apply copper-based bio-fungicides.",
            "Avoid nitrogen fertilizer over-application in spring."
        ],
        "chemical_treatment": [
            "Captan, Pyraclostrobin, or Boscalid."
        ],
        "prevention": [
            "Plant on raised plastic-mulched beds.",
            "Use drip irrigation rather than overhead sprinklers."
        ]
    },
    "Strawberry___healthy": {
        "crop": "Strawberry",
        "disease": "Healthy Plant",
        "scientific_name": "Fragaria × ananassa",
        "pathogen_type": "None",
        "is_healthy": True,
        "severity": "None",
        "symptoms": "Lush trifoliate leaves, uniform deep emerald color, active runnering, unblemished crowns.",
        "causes": "Good straw or plastic mulch, well-draining soil, adequate sunlight.",
        "organic_treatment": [
            "No treatment needed."
        ],
        "chemical_treatment": [
            "None needed."
        ],
        "prevention": [
            "Renew strawberry beds every 3-4 years; maintain straw mulch barrier."
        ]
    },
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "disease": "Bacterial Spot",
        "scientific_name": "Xanthomonas vesicatoria",
        "pathogen_type": "Bacterium",
        "is_healthy": False,
        "severity": "High",
        "symptoms": "Small (less than 3mm), dark brown, water-soaked circular spots on leaves that turn greasy and necrotic. Leaves turn yellow and drop.",
        "causes": "Splashing water, driving rain, warm humid weather (24°C–30°C).",
        "organic_treatment": [
            "Apply copper sulfate or copper hydroxide combined with Bacillus amyloliquefaciens.",
            "Prune lower infected foliage carefully and disinfect shears with 70% alcohol.",
            "Remove severely stunted plants."
        ],
        "chemical_treatment": [
            "Tank-mix copper fungicides with Mancozeb to overcome copper-resistant bacterial strains."
        ],
        "prevention": [
            "Buy certified clean, hot-water-treated tomato seeds.",
            "Use drip irrigation exclusively.",
            "Never work in wet tomato rows."
        ]
    },
    "Tomato___Early_blight": {
        "crop": "Tomato",
        "disease": "Early Blight",
        "scientific_name": "Alternaria solani",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "Moderate to High",
        "symptoms": "Dark brown to black spots with concentric rings resembling a target board. Surrounding tissue turns yellow (chlorosis). Spreads upward from lower leaves.",
        "causes": "Warm temperatures (24°C–29°C), high humidity, frequent rain or overhead dew.",
        "organic_treatment": [
            "Prune off affected lower leaves up to 12 inches above the soil line.",
            "Apply copper fungicide or potassium bicarbonate every 7-10 days.",
            "Apply organic mulch (straw/leaves) under plants to prevent soil splash."
        ],
        "chemical_treatment": [
            "Chlorothalonil, Mancozeb, Azoxystrobin, or Pyraclostrobin."
        ],
        "prevention": [
            "Space tomato plants 24-36 inches apart on sturdy stakes or cages.",
            "Practice 3-year crop rotation away from solanaceous plants.",
            "Always water at the base with soaker hoses."
        ]
    },
    "Tomato___Late_blight": {
        "crop": "Tomato",
        "disease": "Late Blight",
        "scientific_name": "Phytophthora infestans",
        "pathogen_type": "Oomycete",
        "is_healthy": False,
        "severity": "Critical",
        "symptoms": "Large, irregular, pale green to water-soaked brownish-black lesions. In humid weather, delicate white fungal growth appears on underside of leaves. Entire vines collapse rapidly.",
        "causes": "Cool, damp weather (15°C–22°C) with persistent cloud cover and humidity > 90%.",
        "organic_treatment": [
            "Apply protective copper sprays immediately upon disease warning.",
            "Bag and discard heavily infected plants instantly (do not compost).",
            "Keep foliage completely dry inside high tunnels or greenhouses."
        ],
        "chemical_treatment": [
            "Mandipropamid (Revus), Cymoxanil (Curzate), Dimethomorph, or Chlorothalonil."
        ],
        "prevention": [
            "Plant resistant tomato varieties (e.g., Defiant, Mountain Merit, Iron Lady).",
            "Avoid planting near potatoes.",
            "Provide ample ventilation and air drainage."
        ]
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "disease": "Leaf Mold",
        "scientific_name": "Passalora fulva (Cladosporium fulvum)",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "Moderate",
        "symptoms": "Pale greenish-yellow patches on upper leaf surfaces; velvety olive-green to brown mold carpets the corresponding underside of the leaf.",
        "causes": "High relative humidity (>85%) and warm temperatures (21°C–24°C); very common in greenhouses and high tunnels.",
        "organic_treatment": [
            "Increase greenhouse ventilation with exhaust fans.",
            "Apply copper hydroxide or bio-fungicide Serenade (Bacillus subtilis).",
            "Strip bottom leaves to facilitate low-level air movement."
        ],
        "chemical_treatment": [
            "Chlorothalonil, Difenoconazole, or Mancozeb."
        ],
        "prevention": [
            "Use drip irrigation and vent greenhouse night and day.",
            "Choose greenhouse varieties carrying Cf-resistance genes."
        ]
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "disease": "Septoria Leaf Spot",
        "scientific_name": "Septoria lycopersici",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "High",
        "symptoms": "Numerous small (2-3mm) circular spots with dark brown margins and sunken grayish-white centers dotted with tiny black specks (pycnidia). Leaves yellow and drop.",
        "causes": "Warm, wet weather (20°C–25°C); fungal spores splashed up from infected soil debris.",
        "organic_treatment": [
            "Pick off diseased leaves early.",
            "Spray copper fungicide or sulfur every 7 days during rainy spells.",
            "Apply 3-4 inches of clean straw mulch around the base of each plant."
        ],
        "chemical_treatment": [
            "Chlorothalonil, Mancozeb, or Quadris (Azoxystrobin)."
        ],
        "prevention": [
            "Stake or cage plants to keep foliage elevated off soil.",
            "Disinfect stakes with 10% bleach solution between seasons.",
            "Rotate crops annually."
        ]
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato",
        "disease": "Spider Mites (Two-Spotted Spider Mite)",
        "scientific_name": "Tetranychus urticae",
        "pathogen_type": "Arachnid Pest",
        "is_healthy": False,
        "severity": "Moderate to High",
        "symptoms": "Fine yellow, white, or bronze speckling (stippling) on upper leaf surfaces. Undersides show fine webbing, tiny scurrying mites, and bronze dried-out foliage.",
        "causes": "Hot, dry, dusty environmental conditions (>27°C with low humidity).",
        "organic_treatment": [
            "Wash foliage vigorously with strong jets of water to dislodge mites and destroy webbing.",
            "Spray with insecticidal soap, rosemary oil, or neem oil (ensure thorough underside coverage).",
            "Release predatory mites (Phytoseiulus persimilis or Neoseiulus californicus)."
        ],
        "chemical_treatment": [
            "Specific miticides: Bifenazate (Acramite), Spiromesifen, or Abamectin."
        ],
        "prevention": [
            "Maintain soil moisture and reduce dust on roadways and garden borders.",
            "Avoid broad-spectrum synthetic pyrethroids that wipe out beneficial predatory insects."
        ]
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "disease": "Target Spot",
        "scientific_name": "Corynespora cassiicola",
        "pathogen_type": "Fungus",
        "is_healthy": False,
        "severity": "Moderate to High",
        "symptoms": "Pinpoint brown spots expanding into circular lesions with pale brown centers and dark concentric rings. Lesions appear on foliage, stems, and fruit.",
        "causes": "Warm temperatures (20°C–28°C) and high humidity; dense foliage canopies.",
        "organic_treatment": [
            "Apply copper-based fungicides or bio-fungicide Bacillus amyloliquefaciens.",
            "Prune internal suckers to open canopy to light and airflow."
        ],
        "chemical_treatment": [
            "Famoxadone + Cymoxanil, Fluxapyroxad + Pyraclostrobin, or Chlorothalonil."
        ],
        "prevention": [
            "Eliminate solanaceous weeds (nightshade) around the crop perimeter.",
            "Avoid overhead irrigation; prune bottom foliage."
        ]
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "disease": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "scientific_name": "Tomato yellow leaf curl virus (TYLCV)",
        "pathogen_type": "Virus (Vector: Silverleaf Whitefly)",
        "is_healthy": False,
        "severity": "Critical",
        "symptoms": "Severe upward cupping of leaves, yellowing of leaf margins (chlorosis), marked stunting of shoots ('bushy bonsai' appearance), and complete flower abortion.",
        "causes": "Vectored by the silverleaf whitefly (Bemisia tabaci); not seed-borne, not transmitted mechanically by touch.",
        "organic_treatment": [
            "Install yellow sticky cards to monitor and trap adult whiteflies.",
            "Spray insecticidal soaps, paraffinic horticultural oils, or azadirachtin (neem extract).",
            "Immediately bag and rogue out infected plants to protect healthy neighbors."
        ],
        "chemical_treatment": [
            "Systemic insecticides targeting whiteflies: Dinotefuran, Imidacloprid, or Spirotetramat (Movento)."
        ],
        "prevention": [
            "Grow TYLCV-resistant hybrids (e.g., Tycoon, SecuriTY, Charger).",
            "Use fine insect-exclusion netting (50 mesh) in greenhouses."
        ]
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "disease": "Tomato Mosaic Virus (ToMV)",
        "scientific_name": "Tomato mosaic tobamovirus",
        "pathogen_type": "Virus (Mechanically Transmitted)",
        "is_healthy": False,
        "severity": "High",
        "symptoms": "Light and dark green mottling (mosaic) on foliage, leaf distortion, blistered lamina, 'shoestring' narrowing of leaves, and internal brown fruit browning.",
        "causes": "Extremely stable virus transmitted by touch, infected hands/tools, tobacco products, and contaminated seed coats.",
        "organic_treatment": [
            "No chemical cure exists for viral infections.",
            "Wash hands thoroughly with soap or 20% non-fat dry milk solution before handling plants.",
            "Remove and incinerate infected plants immediately."
        ],
        "chemical_treatment": [
            "No chemical cure exists. Disinfect all stakes and tools with 10% household bleach or Virkon S."
        ],
        "prevention": [
            "Sow certified virus-free seeds treated with trisodium phosphate (TSP).",
            "Enforce strict non-smoking rules in or near the tomato field/greenhouse.",
            "Select resistant cultivars designated with 'ToMV' or 'Tm-2^2'."
        ]
    },
    "Tomato___healthy": {
        "crop": "Tomato",
        "disease": "Healthy Plant",
        "scientific_name": "Solanum lycopersicum",
        "pathogen_type": "None",
        "is_healthy": True,
        "severity": "None",
        "symptoms": "Deep emerald-green foliage, vigorous growth, crisp leaves without blemishes, spots, mosaic patterns, or curling.",
        "causes": "Optimal nutrient management (NPK + Calcium), adequate sunlight, drip irrigation, good aeration.",
        "organic_treatment": [
            "No treatment needed.",
            "Apply balanced seaweed extract or compost tea as foliar tonic."
        ],
        "chemical_treatment": [
            "None needed."
        ],
        "prevention": [
            "Maintain consistent drip irrigation, mulch soil, and prune bottom foliage."
        ]
    }
}


def get_disease_info(class_name: str) -> dict:
    """Retrieve detailed disease metadata for a given class name."""
    if class_name in DISEASE_DETAILS:
        info = DISEASE_DETAILS[class_name].copy()
        info["class_key"] = class_name
        return info

    # Fallback if class name is unrecognized
    clean_name = class_name.replace("___", " - ").replace("_", " ")
    return {
        "crop": class_name.split("___")[0].replace("_", " "),
        "disease": clean_name,
        "scientific_name": "Unknown",
        "pathogen_type": "Unknown",
        "is_healthy": "healthy" in class_name.lower(),
        "severity": "Moderate",
        "symptoms": "Visual anomalies detected on the leaf surface.",
        "causes": "Unspecified agricultural condition.",
        "organic_treatment": ["Isolate plant, improve air circulation, avoid leaf wetness."],
        "chemical_treatment": ["Consult local agricultural extension service for lab verification."],
        "prevention": ["Practice regular crop rotation, maintain soil health, clean equipment."],
        "class_key": class_name
    }
