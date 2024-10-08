# Dictionary storing 100 mathquestions including 4 options and answers

mathquestions = [
    {"question": "6 ÷ 2 = ?", "options": [2, 3, 4, 5], "answer": 3},
    {"question": "8 ÷ 4 = ?", "options": [1, 2, 3, 4], "answer": 2},
    {"question": "9 ÷ 3 = ?", "options": [2, 3, 4, 5], "answer": 3},
    {"question": "10 ÷ 2 = ?", "options": [4, 5, 6, 7], "answer": 5},
    {"question": "15 ÷ 5 = ?", "options": [2, 3, 4, 5], "answer": 3},
    {"question": "20 ÷ 4 = ?", "options": [4, 5, 6, 7], "answer": 5},
    {"question": "18 ÷ 6 = ?", "options": [2, 3, 4, 5], "answer": 3},
    {"question": "25 ÷ 5 = ?", "options": [4, 5, 6, 7], "answer": 5},
    {"question": "16 ÷ 4 = ?", "options": [2, 3, 4, 5], "answer": 4},
    {"question": "30 ÷ 6 = ?", "options": [3, 4, 5, 6], "answer": 5},
    {"question": "2 x 3 = ?", "options": [5, 6, 7, 8], "answer": 6},
    {"question": "4 ÷ 2 = ?", "options": [1, 2, 3, 4], "answer": 2},
    {"question": "5 x 4 = ?", "options": [19, 20, 21, 22], "answer": 20},
    {"question": "12 ÷ 4 = ?", "options": [2, 3, 4, 5], "answer": 3},
    {"question": "9 ÷ 9 = ?", "options": [0, 1, 2, 3], "answer": 1},
    {"question": "3 x 5 = ?", "options": [13, 14, 15, 16], "answer": 15},
    {"question": "6 ÷ 3 = ?", "options": [1, 2, 3, 4], "answer": 2},
    {"question": "7 x 6 = ?", "options": [41, 42, 43, 44], "answer": 42},
    {"question": "45 ÷ 9 = ?", "options": [4, 5, 6, 7], "answer": 5},
    {"question": "3 x 4 = ?", "options": [11, 12, 13, 14], "answer": 12},
    {"question": "10 ÷ 2 = ?", "options": [4, 5, 6, 7], "answer": 5},
    {"question": "5 x 7 = ?", "options": [34, 35, 36, 37], "answer": 35},
    {"question": "100 ÷ 10 = ?", "options": [8, 9, 10, 11], "answer": 10},
    {"question": "9 x 9 = ?", "options": [80, 81, 82, 83], "answer": 81},
    {"question": "14 ÷ 7 = ?", "options": [1, 2, 3, 4], "answer": 2},
    {"question": "6 ÷ 2 = ?", "options": [2, 3, 4, 5], "answer": 3},
    {"question": "8 x 3 = ?", "options": [22, 23, 24, 25], "answer": 24},
    {"question": "25 ÷ 5 = ?", "options": [3, 4, 5, 6], "answer": 5},
    {"question": "6 x 6 = ?", "options": [35, 36, 37, 38], "answer": 36},
    {"question": "49 ÷ 7 = ?", "options": [6, 7, 8, 9], "answer": 7},
    {"question": "10 x 3 = ?", "options": [29, 30, 31, 32], "answer": 30},
    {"question": "64 ÷ 8 = ?", "options": [6, 7, 8, 9], "answer": 8},
    {"question": "16 ÷ 2 = ?", "options": [6, 7, 8, 9], "answer": 8},
    {"question": "4 x 4 = ?", "options": [14, 15, 16, 17], "answer": 16},
    {"question": "15 ÷ 3 = ?", "options": [4, 5, 6, 7], "answer": 5},
    {"question": "7 x 5 = ?", "options": [34, 35, 36, 37], "answer": 35},
    {"question": "24 ÷ 6 = ?", "options": [3, 4, 5, 6], "answer": 4},
    {"question": "5 x 8 = ?", "options": [39, 40, 41, 42], "answer": 40},
    {"question": "8 ÷ 2 = ?", "options": [3, 4, 5, 6], "answer": 4},
    {"question": "18 ÷ 3 = ?", "options": [4, 5, 6, 7], "answer": 6},
    {"question": "9 ÷ 3 = ?", "options": [2, 3, 4, 5], "answer": 3},
    {"question": "3 x 9 = ?", "options": [26, 27, 28, 29], "answer": 27},
    {"question": "21 ÷ 7 = ?", "options": [2, 3, 4, 5], "answer": 3},
    {"question": "6 x 4 = ?", "options": [23, 24, 25, 26], "answer": 24},
    {"question": "28 ÷ 4 = ?", "options": [6, 7, 8, 9], "answer": 7},
    {"question": "10 x 5 = ?", "options": [49, 50, 51, 52], "answer": 50},
    {"question": "35 ÷ 5 = ?", "options": [6, 7, 8, 9], "answer": 7},
    {"question": "4 x 9 = ?", "options": [34, 35, 36, 37], "answer": 36},
    {"question": "36 ÷ 6 = ?", "options": [5, 6, 7, 8], "answer": 6},
    {"question": "3 x 10 = ?", "options": [29, 30, 31, 32], "answer": 30},
    {"question": "18 ÷ 9 = ?", "options": [1, 2, 3, 4], "answer": 2},
    {"question": "12 ÷ 6 = ?", "options": [1, 2, 3, 4], "answer": 2},
    {"question": "5 x 5 = ?", "options": [24, 25, 26, 27], "answer": 25},
    {"question": "40 ÷ 5 = ?", "options": [6, 7, 8, 9], "answer": 8},
    {"question": "6 x 7 = ?", "options": [41, 42, 43, 44], "answer": 42},
    {"question": "54 ÷ 9 = ?", "options": [5, 6, 7, 8], "answer": 6},
    {"question": "10 + 5 = ?", "options": [13, 14, 15, 16], "answer": 15},
    {"question": "12 + 8 = ?", "options": [18, 19, 20, 21], "answer": 20},
    {"question": "15 - 6 = ?", "options": [7, 8, 9, 10], "answer": 9},
    {"question": "20 - 8 = ?", "options": [10, 11, 12, 13], "answer": 12},
    {"question": "14 + 7 = ?", "options": [19, 20, 21, 22], "answer": 21},
    {"question": "30 - 10 = ?", "options": [18, 19, 20, 21], "answer": 20},
    {"question": "9 + 8 = ?", "options": [16, 17, 18, 19], "answer": 17},
    {"question": "18 - 9 = ?", "options": [8, 9, 10, 11], "answer": 9},
    {"question": "25 + 15 = ?", "options": [38, 39, 40, 41], "answer": 40},
    {"question": "50 - 20 = ?", "options": [30, 31, 32, 33], "answer": 30},
    {"question": "12 + 5 = ?", "options": [16, 17, 18, 19], "answer": 17},
    {"question": "9 - 4 = ?", "options": [4, 5, 6, 7], "answer": 5},
    {"question": "7 + 3 = ?", "options": [9, 10, 11, 12], "answer": 10},
    {"question": "11 - 5 = ?", "options": [5, 6, 7, 8], "answer": 6},
]

geographyquestions = [
    {
        "question": "What is the capital of Nepal? 🇳🇵",
        "options": [
            "1: Kathmandu",
            "2: Pokhara",
            "3: Biratnagar",
            "4: Lalitpur",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of France? 🇫🇷",
        "options": ["1: Lyon", "2: Marseille", "3: Paris", "4: Nice"],
        "answer": 3,
    },
    {
        "question": "What is the capital of Japan? 🇯🇵",
        "options": ["1: Kyoto", "2: Tokyo", "3: Osaka", "4: Nagoya"],
        "answer": 2,
    },
    {
        "question": "What is the capital of Australia? 🇦🇺",
        "options": ["1: Sydney", "2: Melbourne", "3: Canberra", "4: Perth"],
        "answer": 3,
    },
    {
        "question": "What is the capital of Brazil? 🇧🇷",
        "options": [
            "1: Rio de Janeiro",
            "2: São Paulo",
            "3: Brasilia",
            "4: Salvador",
        ],
        "answer": 3,
    },
    {
        "question": "What is the capital of Canada? 🇨🇦",
        "options": ["1: Ottawa", "2: Toronto", "3: Vancouver", "4: Montreal"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Germany? 🇩🇪",
        "options": ["1: Hamburg", "2: Munich", "3: Frankfurt", "4: Berlin"],
        "answer": 4,
    },
    {
        "question": "What is the capital of Italy? 🇮🇹",
        "options": ["1: Venice", "2: Milan", "3: Rome", "4: Florence"],
        "answer": 3,
    },
    {
        "question": "What is the capital of Russia? 🇷🇺",
        "options": [
            "1: Saint Petersburg",
            "2: Moscow",
            "3: Kazan",
            "4: Novosibirsk",
        ],
        "answer": 2,
    },
    {
        "question": "What is the capital of China? 🇨🇳",
        "options": ["1: Beijing", "2: Shanghai", "3: Guangzhou", "4: Chengdu"],
        "answer": 1,
    },
    {
        "question": "What is the capital of India? 🇮🇳",
        "options": ["1: Mumbai", "2: Delhi", "3: Kolkata", "4: New Delhi"],
        "answer": 4,
    },
    {
        "question": "What is the capital of South Korea? 🇰🇷",
        "options": ["1: Busan", "2: Seoul", "3: Incheon", "4: Daejeon"],
        "answer": 2,
    },
    {
        "question": "What is the capital of Mexico? 🇲🇽",
        "options": [
            "1: Guadalajara",
            "2: Tijuana",
            "3: Mexico City",
            "4: Monterrey",
        ],
        "answer": 3,
    },
    {
        "question": "What is the capital of Egypt? 🇪🇬",
        "options": ["1: Alexandria", "2: Cairo", "3: Giza", "4: Luxor"],
        "answer": 2,
    },
    {
        "question": "What is the capital of Argentina? 🇦🇷",
        "options": [
            "1: Buenos Aires",
            "2: Córdoba",
            "3: Rosario",
            "4: Mendoza",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Spain? 🇪🇸",
        "options": ["1: Barcelona", "2: Valencia", "3: Madrid", "4: Seville"],
        "answer": 3,
    },
    {
        "question": "What is the capital of the United Kingdom? 🇬🇧",
        "options": [
            "1: Manchester",
            "2: Birmingham",
            "3: Edinburgh",
            "4: London",
        ],
        "answer": 4,
    },
    {
        "question": "What is the capital of Greece? 🇬🇷",
        "options": [
            "1: Athens",
            "2: Thessaloniki",
            "3: Heraklion",
            "4: Patras",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Portugal? 🇵🇹",
        "options": ["1: Porto", "2: Lisbon", "3: Faro", "4: Braga"],
        "answer": 2,
    },
    {
        "question": "What is the capital of Turkey? 🇹🇷",
        "options": ["1: Istanbul", "2: Ankara", "3: Izmir", "4: Antalya"],
        "answer": 2,
    },
    {
        "question": "What is the capital of South Africa? 🇿🇦",
        "options": [
            "1: Cape Town",
            "2: Johannesburg",
            "3: Pretoria",
            "4: Durban",
        ],
        "answer": 3,
    },
    {
        "question": "What is the capital of Saudi Arabia? 🇸🇦",
        "options": ["1: Mecca", "2: Jeddah", "3: Riyadh", "4: Medina"],
        "answer": 3,
    },
    {
        "question": "What is the capital of Thailand? 🇹🇭",
        "options": ["1: Bangkok", "2: Chiang Mai", "3: Pattaya", "4: Phuket"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Sweden? 🇸🇪",
        "options": ["1: Stockholm", "2: Gothenburg", "3: Malmö", "4: Uppsala"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Norway? 🇳🇴",
        "options": ["1: Oslo", "2: Bergen", "3: Stavanger", "4: Trondheim"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Finland? 🇫🇮",
        "options": ["1: Turku", "2: Helsinki", "3: Tampere", "4: Oulu"],
        "answer": 2,
    },
    {
        "question": "What is the capital of Denmark? 🇩🇰",
        "options": ["1: Aarhus", "2: Copenhagen", "3: Odense", "4: Aalborg"],
        "answer": 2,
    },
    {
        "question": "What is the capital of Iceland? 🇮🇸",
        "options": [
            "1: Reykjavik",
            "2: Akureyri",
            "3: Selfoss",
            "4: Keflavik",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of New Zealand? 🇳🇿",
        "options": [
            "1: Wellington",
            "2: Auckland",
            "3: Christchurch",
            "4: Dunedin",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of the Philippines? 🇵🇭",
        "options": [
            "1: Manila",
            "2: Cebu City",
            "3: Davao City",
            "4: Quezon City",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Indonesia? 🇮🇩",
        "options": ["1: Jakarta", "2: Bali", "3: Surabaya", "4: Medan"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Malaysia? 🇲🇾",
        "options": [
            "1: Kuala Lumpur",
            "2: George Town",
            "3: Johor Bahru",
            "4: Kuching",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Singapore? 🇸🇬",
        "options": ["1: Singapore", "2: Sentosa", "3: Jurong", "4: Yishun"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Vietnam? 🇻🇳",
        "options": [
            "1: Hanoi",
            "2: Ho Chi Minh City",
            "3: Da Nang",
            "4: Hai Phong",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of the United Arab Emirates? 🇦🇪",
        "options": [
            "1: Abu Dhabi",
            "2: Dubai",
            "3: Sharjah",
            "4: Ras Al Khaimah",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Iraq? 🇮🇶",
        "options": ["1: Baghdad", "2: Mosul", "3: Basra", "4: Erbil"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Iran? 🇮🇷",
        "options": ["1: Tehran", "2: Isfahan", "3: Mashhad", "4: Shiraz"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Afghanistan? 🇦🇫",
        "options": [
            "1: Kabul",
            "2: Kandahar",
            "3: Herat",
            "4: Mazar-i-Sharif",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Bangladesh? 🇧🇩",
        "options": ["1: Dhaka", "2: Chittagong", "3: Khulna", "4: Sylhet"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Pakistan? 🇵🇰",
        "options": ["1: Islamabad", "2: Karachi", "3: Lahore", "4: Peshawar"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Chile? 🇨🇱",
        "options": [
            "1: Santiago",
            "2: Valparaíso",
            "3: Concepción",
            "4: Antofagasta",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Colombia? 🇨🇴",
        "options": ["1: Bogotá", "2: Medellín", "3: Cali", "4: Cartagena"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Venezuela? 🇻🇪",
        "options": [
            "1: Caracas",
            "2: Maracaibo",
            "3: Valencia",
            "4: Barquisimeto",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Peru? 🇵🇪",
        "options": ["1: Lima", "2: Cusco", "3: Arequipa", "4: Trujillo"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Bolivia? 🇧🇴",
        "options": ["1: La Paz", "2: Sucre", "3: Cochabamba", "4: Santa Cruz"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Paraguay? 🇵🇾",
        "options": [
            "1: Asunción",
            "2: Ciudad del Este",
            "3: Encarnación",
            "4: Luque",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Uruguay? 🇺🇾",
        "options": [
            "1: Montevideo",
            "2: Salto",
            "3: Punta del Este",
            "4: Colonia",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Ecuador? 🇪🇨",
        "options": ["1: Quito", "2: Guayaquil", "3: Cuenca", "4: Ambato"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Panama? 🇵🇦",
        "options": ["1: Panama City", "2: Colón", "3: David", "4: Santiago"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Costa Rica? 🇨🇷",
        "options": ["1: San José", "2: Alajuela", "3: Heredia", "4: Cartago"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Honduras? 🇭🇳",
        "options": [
            "1: Tegucigalpa",
            "2: San Pedro Sula",
            "3: La Ceiba",
            "4: Comayagua",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Guatemala? 🇬🇹",
        "options": [
            "1: Guatemala City",
            "2: Antigua",
            "3: Quetzaltenango",
            "4: Escuintla",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of El Salvador? 🇸🇻",
        "options": [
            "1: San Salvador",
            "2: Santa Ana",
            "3: San Miguel",
            "4: Sonsonate",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Nicaragua? 🇳🇮",
        "options": ["1: Managua", "2: León", "3: Granada", "4: Masaya"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Belize? 🇧🇿",
        "options": [
            "1: Belmopan",
            "2: Belize City",
            "3: San Ignacio",
            "4: Orange Walk",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Cuba? 🇨🇺",
        "options": [
            "1: Havana",
            "2: Santiago de Cuba",
            "3: Camagüey",
            "4: Holguín",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Haiti? 🇭🇹",
        "options": [
            "1: Port-au-Prince",
            "2: Cap-Haïtien",
            "3: Jacmel",
            "4: Gonaïves",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of the Dominican Republic? 🇩🇴",
        "options": [
            "1: Santo Domingo",
            "2: Santiago de los Caballeros",
            "3: La Romana",
            "4: Puerto Plata",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Jamaica? 🇯🇲",
        "options": [
            "1: Kingston",
            "2: Montego Bay",
            "3: Ocho Rios",
            "4: Portmore",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Trinidad and Tobago? 🇹🇹",
        "options": [
            "1: Port of Spain",
            "2: San Fernando",
            "3: Chaguanas",
            "4: Arima",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Barbados? 🇧🇧",
        "options": [
            "1: Bridgetown",
            "2: Speightstown",
            "3: Oistins",
            "4: Holetown",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of the Bahamas? 🇧🇸",
        "options": ["1: Nassau", "2: Freeport", "3: Eleuthera", "4: Exuma"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Saint Lucia? 🇱🇨",
        "options": [
            "1: Castries",
            "2: Soufrière",
            "3: Vieux Fort",
            "4: Gros Islet",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Grenada? 🇬🇩",
        "options": [
            "1: St. George's",
            "2: Gouyave",
            "3: Hillsborough",
            "4: Victoria",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of\
             Saint Vincent and the Grenadines? 🇻🇨",
        "options": [
            "1: Kingstown",
            "2: Barrouallie",
            "3: Georgetown",
            "4: Chateaubelair",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Antigua and Barbuda? 🇦🇬",
        "options": [
            "1: St. John's",
            "2: Codrington",
            "3: All Saints",
            "4: English Harbour",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Saint Kitts and Nevis? 🇰🇳",
        "options": [
            "1: Basseterre",
            "2: Charlestown",
            "3: Sandy Point",
            "4: Dieppe Bay",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Dominica? 🇩🇲",
        "options": [
            "1: Roseau",
            "2: Portsmouth",
            "3: Marigot",
            "4: Castle Bruce",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Suriname? 🇸🇷",
        "options": [
            "1: Paramaribo",
            "2: Lelydorp",
            "3: Nieuw Nickerie",
            "4: Moengo",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Guyana? 🇬🇾",
        "options": [
            "1: Georgetown",
            "2: Linden",
            "3: New Amsterdam",
            "4: Bartica",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Fiji? 🇫🇯",
        "options": ["1: Suva", "2: Nadi", "3: Lautoka", "4: Labasa"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Papua New Guinea? 🇵🇬",
        "options": [
            "1: Port Moresby",
            "2: Lae",
            "3: Mount Hagen",
            "4: Madang",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Samoa? 🇼🇸",
        "options": [
            "1: Apia",
            "2: Salelologa",
            "3: Safotulafai",
            "4: Mulifanua",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Tonga? 🇹🇴",
        "options": ["1: Nuku'alofa", "2: Neiafu", "3: Pangai", "4: Kolonga"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Vanuatu? 🇻🇺",
        "options": [
            "1: Port Vila",
            "2: Luganville",
            "3: Isangel",
            "4: Lenakel",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of the Solomon Islands? 🇸🇧",
        "options": ["1: Honiara", "2: Gizo", "3: Auki", "4: Tulagi"],
        "answer": 1,
    },
    {
        "question": "What is the capital of the Marshall Islands? 🇲🇭",
        "options": ["1: Majuro", "2: Ebeye", "3: Kwajalein", "4: Jaluit"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Micronesia? 🇫🇲",
        "options": ["1: Palikir", "2: Weno", "3: Yap", "4: Kolonia"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Kiribati? 🇰🇮",
        "options": [
            "1: Tarawa",
            "2: Kiritimati",
            "3: Bikenibeu",
            "4: Abaiang",
        ],
        "answer": 1,
    },
    {
        "question": "What is the capital of Palau? 🇵🇼",
        "options": ["1: Ngerulmud", "2: Koror", "3: Airai", "4: Ngchesar"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Tuvalu? 🇹🇻",
        "options": ["1: Funafuti", "2: Nanumea", "3: Nukufetau", "4: Vaitupu"],
        "answer": 1,
    },
    {
        "question": "What is the capital of North Macedonia? 🇲🇰",
        "options": ["1: Skopje", "2: Bitola", "3: Ohrid", "4: Tetovo"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Albania? 🇦🇱",
        "options": ["1: Tirana", "2: Durrës", "3: Shkodër", "4: Vlora"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Montenegro? 🇲🇪",
        "options": ["1: Podgorica", "2: Nikšić", "3: Cetinje", "4: Kotor"],
        "answer": 1,
    },
    {
        "question": "What is the capital of Kosovo? 🇽🇰",
        "options": ["1: Pristina", "2: Mitrovica", "3: Peć", "4: Prizren"],
        "answer": 1,
    },
]
