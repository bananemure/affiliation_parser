# keyword list

DEPARMENT = frozenset(['laboratorio', 'laboratories', 'laboratory',
    'laboratoire', 'institute', 'academic', 'department', 'division',
    'faculty of ', 'genomics center', 'research station'])

INSTITUTE = frozenset(['college', 'university', 'universitat', 'universite',
    'unversiteit', 'universita', 'universidad', 'universiti', 'hospital', 'hopitaux de', 'unidade de',
    "ha'pital", 'istituti', 'istituto', 'institucio', 'institut', 'medical center', ' pharma',
    'riuniti', 'clinic', ' school of medicine', 'karolinska sjukhuset',
    'national institutes of health', 'cancer center', 'bioscience institute',
    'national institute for', 'national center for ', 'national centre for',
    'unilever research', 'national cardiovascular center',
    'centro operativo', 'animal research centre', 'nutrition research center',
    'national perinatal epidemiology unit', 'tanabe seiyaku', 'animal health trust',
    'marine biological laboratory', ' medical school', ' research laboratories',
    'baxter diagnostics', 'inserm', 'sylvius laboratory', 'broad institute', ' inra', '/inra',
    'health chemical laboratory', 'genecor, inc', 'infirmary',
    'national center for health', 'john innes centre', 'chru de la timone',
    'chu de bordeaux', 'ecole nationale ', 'cape technologies',
    'national chemical laboratory', ' national laboratory', 'department of research and development',
    'academy of sciences', 'centre chirurgical de la porte', 'international centre of ',
    'lawrence berkeley laboratory', 'albert einstein college', 'gedeon richter ltd',
    ' nih', 'ufrgs', 'national research centre', ' co.', ' ltd.', ' ltd', 'inc.', 'research limited',
    'clinic college of', 'center for', 'research center', 'research centre',
    'schon klinik', 'innovaderm research', 'novartis', 'aquarium', 'foundation',
    'permanente', 'healthcare system', 'national oncology institute',
    'global research and development', 'health service', 'national primate research center',
    'faculdade de ', ' urmc', ' pllc', ' pgimer', 'center for disease control',
    'london school of ', 'ggze', 'health service executive', 'council for scientific',
    'cnrs', 'eth zurich', 'johns hopkins', 'isconova', 'barts health', 'ceinge',
    'national jewish health', 'german institute', 'iqwig', 'federal joint committee'
    'nationale contre', 'cura villa maria', 'centre de psychologie', 'centro diagnostico',
    'international reference centre', 'complesso integrato', 'health care centre',
    'idiphim', 'cytogenetic laboratory', 'fondazione', 'facebook', 'google', 'association for',
    ' llc', 'national museum', 'national research council', 'rehabilitation center',
    'rehabilitation institute', 'oncology center', 'cancer centre', 'virginia tech',
    'ciberesp', 'department of food', 'rothamsted research', 'evangelisches',
    'ziekenhuizen', 'academy of ', 'chinese national ', 'pathology associates',
    'science magnet', 'ucla ', ' ucsd', 'uc berkeley', 'uc san diego', 'trial group',
    'acdi', 'specialty center', 'agemetra', 'national research institute', 'diabetes center',
    'rothamsted research', 'affichem', 'disease association', 'ministry of health',
    'incorporation', 'medical research council', 'develogen', 'innovation campus',
    'flemish government', "centre d'etudes", 'kaist', 'epfl', ' eth', 'ecole normale',
    'ecole polytechnique', 'mental health center', 'charite centrum', 'phc affairs',
    'afmc', 'cdsr', 'chu de ', 'harvard school', 'karnavati school', 'academic centre for',
    'school of public health', 'school of sport sciences', 'medical center', 'medical centre',
    'neocodex', 'umc utrecht', 'centers for disease', 'cardiac surgery center',
    'medical city', 'wisconsin department', "doctor's data", 'drug development office',
    'research unit', 'ecogen', 'international corporation', 'tourism agency',
    'naval research laboratory', 'infection research', 'health solutions',
    'us military', 'us department', 'human genome center', 'siemens', 'swiss institute',
    'usda', 'marine science center', 'u.s. geological', 'u.s. positive', 'u.s. Department',
    'botanical center', 'municipal centre', 'municipal health', 'research council',
    'national serology', 'national sexually', "d'aragona", 'metropolitan health',
    'rosa and company', 'laboratory of oncology', 'oncology r&d', 'assessment service',
    'cancer registry', 'technology agency', 'district health', 'irccs', 'pharmexa',
    'scientific service', 'limited company', 'health authority', 'biodiversity center',
    'national park', 'corporation', 'ucl ', 'escola nacional', 'va health system',
    'agri-food', 'agrotech', 'agroforestry', 'umr micalis', 'allan rosenfield',
    'allan wilson', 'allen institute', 'ameripath', 'biotechnologies', 'anaerobe systems',
    'nhs trust'])

REMOVE_INSTITUE = frozenset(['pharmacology', 'college of pharmacy',
    'institute of zoology', 'institute of population', 'institute of bioinformatics',
    'institute of plant',  'section for ', 'institute of clinical medicine',
    'department of clinical'])

COUNTRY = (
    ('italy', 'italia', 'torino', 'turin', 'portici'),
    ('united kingdom', 'u.k.', '\buk\b', 'uk.', 'england', ' uk', 'liverpool',
     'london', 'crumpsall', 'leicester', 'manchester', 'cardiff', 'salford',
     'bradford', 'oxford', 'clwyd'),
    ('united states of america', 'u.s.a', 'u. s. a.', 'united states', 'massachusetts',
     'boston', 'howard university', 'torrance', 'san francisco', 'duarte', 'los alamos'),
    ('germany', 'frg', 'brd', 'f.r.g.', 'deutschland', 'engelskirchen', 'berlin',
     'hannover', 'marburg', 'mainz', 'leipzig', 'frankfurt'),
    ('japan', 'keio University', 'jikei university', 'shiga university', 'jikei university',
     'niigata university', 'sendai city', 'shiba', 'asahikawa',
     'tokyo', 'yokohama', 'osaka', 'nagoya', 'sapporo', 'kobe', 'kyoto',
     'fukuoka', 'kawasaki', 'saitama', 'hiroshima', 'sendai', 'kitakyushu',
     'chiba', 'sakai', 'hamamatsu', 'niigata', 'shizuoka', 'okayama', 'asahikawa',
     'yamaguchi', 'okayama', 'gunma', 'hyogo', 'kanazawa', 'fukui', 'tajimi',
     'komagome', 'akita', 'suita', 'kochi', 'nara medical', 'keio', 'kobe university',
     'gunma', 'gifu university'),
    ('korea', 'seoul'),
    ('russia', 'moscow'),
    ('austria', 'linz', 'wien', ' graz', 'innsbruck'),
    ('israel', 'jerusalem', 'haifa', 'tel aviv'),
    ('norway', ' oslo'),
    ('finland', 'helsinki'),
    ('south africa', 'johannesburg'),
    ('france', 'paris', 'marseille', 'brest', 'limoges', 'toulouse'),
    ('canada', 'vancouver', 'ontario', 'ottawa', 'nova scotia', 'calgary', 'alberta'),
    ('denmark', 'copenhagen'),
    ('taiwan', 'taiwan, ', 'taipei'),
    ('china', 'beijing', 'pr china', 'hangzhou', 'zhejiang', 'shenyang', 'shanghai'),
    ('egypt', 'cairo'),
    ('poland', 'gdansk', 'krakow'),
    ('turkey', 'istanbul', ' ankara'),
    ('netherlands', 'utrecht', 'nijmegen', 'amsterdam', 'leiden'),
    ('belgium', 'belgique', ' namur', 'bruxelles', ' genk'),
    ('sweden', 'karlstad', 'uppsala', 'stockholm'),
    ('australia', ' perth', 'queensland', 'canberra', 'melbourne'),
    ('south africa', 'johannesburg', 'onderstepoort', 'pretoria'),
    ('hungary', 'ungarn'),
    (' india', 'chandigarh', 'hyderabad', 'delhi', 'calcutta', 'wardha', ' ucms',
     'ludhiana', 'vellore'),
    ('ireland', 'dublin', 'belfast'),
    ('colombia', 'bogota'),
    ('spain', ' madrid', ' toledo', ' alicante', 'zaragoza', 'saragossa', 'barcelona',
     'hospital vega baja', 'valencia', 'malaga'),
    ('greece', 'athens'),
    ('new zealand', 'upper hutt', 'auckland'),
    ('saudi arabia', 'riyadh'),
    ('nigeria', 'ibadan'),
    ('yugoslavia', 'belgrade'),
    ('switzerland', 'basel', ' geneva'),
    ('brazil', 'rio de janeiro'),
    ('thailand', 'bangkok'),
    ('argentina', 'buenos aires'),
    ('tunisia', 'tunis', 'tunisie'),
    ('czech republic', ' praha', 'prague', 'czechoslovakia'),
    ('hungary', 'budapest'),
    ('zimbabwe', 'bulawayo'),
    ('malaysia', 'kelantan'),
    ('vietnam', 'hanoi'),
    ('hong kong', 'hong kong'),
    (' iran', 'tehran', 'shiraz', 'mashhad'),
    ('brazil', 'brasil', 'rio de janeiro', 'cordeiropolis'),
    ('mexico', 'mexico city'),
    ('edinburgh', 'edinburge'),
    ('romania', 'bucharest'),
    ('congo', 'democratic republic of congo'),
    ('armenia', 'yerevan'),
    ('bosnia', 'herzegovina'),
    ('albania', 'tirana'),
    ('tanzania', 'morogoro'),
    ('sri lanka', 'sri lanka'),
    ('cyprus', 'nicosia'),
    ('gambia', ' banjul')
)

STATES = frozenset(['Alabama', 'Alaska', 'Arizona', 'Arkansas',
    'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
    'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
    'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
    'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
    'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
    'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
    'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
    'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
    'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'Washington DC',
    ' AL', ' AK', ' AZ', ' AR', ' CA', ' CO', ' CT', ' DE', ' FL', ' GA ', ' GA,', ' HI',
    ' ID', ' IL', ' IN', ' IA', ' KS', ' KY', ' LA', ' ME', ' MD', ' MA,', ' MA ', ' MI',
    ' MN', ' MS', ' MO', ' MT', ' NE', ' NV', ' NH', ' NJ', ' NM', ' NY', ' NC',
    ' ND', ' OH', ' OK', ' OR', ' PA', ' RI', ' SC', ' SD', ' TN', ' TX', ' UT',
    ' VT', ' VA', ' WA', ' WV', ' WI', ' WY', ' DC'])

UNIVERSITY_DUBLICATE = (
    ('university of california los angeles', 'ucla')
)
