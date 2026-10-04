const categoryStyles=document.createElement('link');categoryStyles.rel='stylesheet';categoryStyles.href='category-pages.css';document.head.appendChild(categoryStyles);
const arabwoodStyles=document.createElement('style');arabwoodStyles.textContent=`
.collection-card{display:block;color:inherit;text-decoration:none}.collection-card .collection-arrow{font-size:28px;line-height:1}.collection-card:hover .collection-arrow{background:var(--gold);color:#050505;border-color:var(--gold)}
.collection-page .page-hero-content h1{font-size:clamp(80px,12vw,170px)}
.video-modal iframe{display:block;width:100%;aspect-ratio:16/9;max-height:74svh;border:1px solid rgba(255,255,255,.16);background:#000;box-shadow:0 30px 90px rgba(0,0,0,.55)}
.video-modal iframe[hidden],.video-modal video[hidden]{display:none}.video-modal.youtube-video .video-modal-inner{width:min(1180px,100%)}
`;document.head.appendChild(arabwoodStyles);

// Portfolio data captured from the published site on 2026-10-04.
// Keep this object JSON-compatible for the repository maintenance scripts.
const categoryData = {
  "commercial": {
    "title": "Commercial & Branded Content",
    "kicker": "Advertising",
    "description": "Commercials, campaigns and promotional content edited for brands and organizations.",
    "cover": "assets/toto-link-commercial.webp",
    "projects": [
      {
        "title": "ToTo Link",
        "subtitle": "Commercial · Video Editing",
        "index": "AD01",
        "image": "assets/toto-link-commercial.webp",
        "video": "assets/toto-link-commercial.mp4",
        "badge": "Watch Ad"
      },
      {
        "title": "SATUC",
        "subtitle": "Branded Promo · Video Editing",
        "index": "AD02",
        "image": "assets/satuc-branded-promo.webp",
        "video": "assets/satuc-branded-promo.mp4",
        "badge": "Watch Promo"
      },
      {
        "title": "Shnider",
        "subtitle": "Commercial · Video Editing",
        "index": "AD03",
        "image": "https://i.ytimg.com/vi/SYQvIrjg8qw/hqdefault.jpg",
        "imageFallback": "assets/toto-link-commercial.webp",
        "youtube": "SYQvIrjg8qw",
        "badge": "Watch Ad"
      }
    ]
  },
  "tv-programs": {
    "title": "TV Programs",
    "kicker": "Television",
    "description": "Programs, formats, channel content and television promos.",
    "cover": "assets/on-e.webp",
    "projects": [
      {
        "title": "On the Road",
        "subtitle": "TV Program · Video Collection",
        "index": "TV01",
        "image": "https://i.ytimg.com/vi/fiNaW_oMzCo/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "collection": "on-the-road",
        "badge": "Open Collection"
      },
      {
        "title": "ArabWood",
        "subtitle": "Entertainment Program · Video Collection",
        "index": "TV02",
        "image": "https://i.ytimg.com/vi/sCGh1JRMK3E/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "collection": "arabwood",
        "badge": "Open Collection"
      },
      {
        "title": "Bel Quran Ehtadayt — Kuwait",
        "subtitle": "TV Program · Video Collection",
        "index": "TV03",
        "image": "https://i.ytimg.com/vi/VPg1fotF0wI/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "collection": "bil-quran-ihtadayt",
        "badge": "Open Collection"
      },
      {
        "title": "Faseero — Kuwait",
        "subtitle": "TV Program · Video Collection",
        "index": "TV04",
        "image": "https://i.ytimg.com/vi/qUToplfiB2s/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "collection": "faseero",
        "badge": "Open Collection"
      },
      {
        "title": "Program MAKHMAK — Platform SHASHA Kuwait",
        "subtitle": "TV Program · SHASHA Kuwait",
        "index": "TV05",
        "image": "https://i.ytimg.com/vi/mkJ6DVwDMjQ/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "collection": "makhmak",
        "badge": "Open Collection"
      },
      {
        "title": "Program Bedaya",
        "subtitle": "TV Program · Video Collection",
        "index": "TV06",
        "image": "https://i.ytimg.com/vi/3e-CpvJaMIg/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "collection": "bedaya",
        "badge": "Open Collection"
      },
      {
        "title": "My Guest with Moataz El Demerdash",
        "subtitle": "TV Program · Video Collection",
        "index": "TV09",
        "image": "https://i.ytimg.com/vi/_5EHAht5a1M/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "collection": "my-guest-moataz-el-demerdash",
        "badge": "Open Collection"
      }
    ],
    "collections": {
      "on-the-road": {
        "title": "On the Road",
        "kicker": "TV Program",
        "description": "Selected On the Road shorts and social edits.",
        "cover": "https://i.ytimg.com/vi/fiNaW_oMzCo/hqdefault.jpg",
        "projects": [
          {
            "title": "Back After 25 Years",
            "subtitle": "On the Road · Short Edit",
            "index": "OTR01",
            "image": "https://i.ytimg.com/vi/fiNaW_oMzCo/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "fiNaW_oMzCo",
            "badge": "Watch Video"
          },
          {
            "title": "First Journey",
            "subtitle": "On the Road · Short Edit",
            "index": "OTR02",
            "image": "https://i.ytimg.com/vi/_irKRUCkujM/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "_irKRUCkujM",
            "badge": "Watch Video"
          },
          {
            "title": "Teaser Nelly Karim_02",
            "subtitle": "On the Road · Short Edit",
            "index": "OTR03",
            "image": "https://i.ytimg.com/vi/YA6XVuavmx4/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "YA6XVuavmx4",
            "badge": "Watch Video"
          },
          {
            "title": "Teaser Nelly Karim_01",
            "subtitle": "On the Road · Short Edit",
            "index": "OTR04",
            "image": "https://i.ytimg.com/vi/UkZ7oWR22zk/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "UkZ7oWR22zk",
            "badge": "Watch Video"
          }
        ]
      },
      "arabwood": {
        "title": "ArabWood",
        "kicker": "Entertainment Program",
        "description": "Selected entertainment edits and event coverage created for ArabWood.",
        "cover": "https://i.ytimg.com/vi/sCGh1JRMK3E/hqdefault.jpg",
        "projects": [
          {
            "title": "Promo General",
            "subtitle": "ArabWood · Program Promo",
            "index": "AW01",
            "image": "https://i.ytimg.com/vi/sCGh1JRMK3E/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "sCGh1JRMK3E",
            "badge": "Watch Video"
          },
          {
            "title": "Giorgio Armani",
            "subtitle": "ArabWood · Entertainment Edit",
            "index": "AW02",
            "image": "https://i.ytimg.com/vi/hO5xZWLdrTo/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "hO5xZWLdrTo",
            "badge": "Watch Video"
          },
          {
            "title": "Emmy Awards 2025",
            "subtitle": "ArabWood · Event Edit",
            "index": "AW03",
            "image": "https://i.ytimg.com/vi/sCjBAIkHqQw/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "sCjBAIkHqQw",
            "badge": "Watch Video"
          },
          {
            "title": "Brand Personality",
            "subtitle": "ArabWood · Brand Edit",
            "index": "AW04",
            "image": "https://i.ytimg.com/vi/Me1dDAzhkVM/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "Me1dDAzhkVM",
            "badge": "Watch Video"
          },
          {
            "title": "Salma Hayek",
            "subtitle": "ArabWood · Entertainment Edit",
            "index": "AW05",
            "image": "https://i.ytimg.com/vi/18Ghd_t5W2E/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "18Ghd_t5W2E",
            "badge": "Watch Video"
          },
          {
            "title": "Reel Salma",
            "subtitle": "ArabWood · Short Edit",
            "index": "AW06",
            "image": "https://i.ytimg.com/vi/6-UYL8iSvr4/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "6-UYL8iSvr4",
            "badge": "Watch Video"
          },
          {
            "title": "Reel Easel",
            "subtitle": "ArabWood · Short Edit",
            "index": "AW07",
            "image": "https://i.ytimg.com/vi/BYcajbe-aUU/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "BYcajbe-aUU",
            "badge": "Watch Video"
          },
          {
            "title": "Bridal Reel",
            "subtitle": "ArabWood · Short Edit",
            "index": "AW08",
            "image": "https://i.ytimg.com/vi/V6ujs3xAFh4/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "V6ujs3xAFh4",
            "badge": "Watch Video"
          }
        ]
      },
      "bil-quran-ihtadayt": {
        "title": "Bel Quran Ehtadayt — Kuwait",
        "kicker": "TV Program",
        "description": "Selected episodes and edits from Bel Quran Ehtadayt — Kuwait.",
        "cover": "https://i.ytimg.com/vi/VPg1fotF0wI/hqdefault.jpg",
        "projects": [
          {
            "title": "Promo | bel Quran",
            "subtitle": "Bel Quran Ehtadayt — Kuwait · TV Program Edit",
            "index": "BQ01",
            "image": "https://i.ytimg.com/vi/VPg1fotF0wI/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "VPg1fotF0wI",
            "badge": "Watch Video"
          },
          {
            "title": "Promo bel Quran",
            "subtitle": "Bel Quran Ehtadayt — Kuwait · TV Program Edit",
            "index": "BQ02",
            "image": "https://i.ytimg.com/vi/LIxN5p9Ymp8/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "LIxN5p9Ymp8",
            "badge": "Watch Video"
          },
          {
            "title": "General bel Quran",
            "subtitle": "Bel Quran Ehtadayt — Kuwait · TV Program Edit",
            "index": "BQ03",
            "image": "https://i.ytimg.com/vi/n9-uUhq2jjg/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "n9-uUhq2jjg",
            "badge": "Watch Video"
          },
          {
            "title": "teaser Bel Qurean_01",
            "subtitle": "Bel Quran Ehtadayt — Kuwait · TV Program Edit",
            "index": "BQ04",
            "image": "https://i.ytimg.com/vi/dIw9LM6kOaE/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "dIw9LM6kOaE",
            "badge": "Watch Video"
          },
          {
            "title": "teaser Bel Qurean_02",
            "subtitle": "Bel Quran Ehtadayt — Kuwait · TV Program Edit",
            "index": "BQ05",
            "image": "https://i.ytimg.com/vi/M8QicqBdPhs/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "M8QicqBdPhs",
            "badge": "Watch Video"
          }
        ]
      },
      "faseero": {
        "title": "Faseero — Kuwait",
        "kicker": "TV Program",
        "description": "Selected work from Faseero — Kuwait.",
        "cover": "https://i.ytimg.com/vi/qUToplfiB2s/hqdefault.jpg",
        "projects": [
          {
            "title": "Promo Faseero",
            "subtitle": "Faseero — Kuwait · TV Program Edit",
            "index": "FS01",
            "image": "https://i.ytimg.com/vi/qUToplfiB2s/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "qUToplfiB2s",
            "badge": "Watch Video"
          }
        ]
      },
      "makhmak": {
        "title": "Program MAKHMAK — Platform SHASHA Kuwait",
        "kicker": "TV Program",
        "description": "Selected work from MAKHMAK on SHASHA Kuwait.",
        "cover": "https://i.ytimg.com/vi/mkJ6DVwDMjQ/hqdefault.jpg",
        "projects": [
          {
            "title": "Promo MAKHMAK",
            "subtitle": "MAKHMAK · SHASHA Kuwait · Video Editing",
            "index": "MK01",
            "image": "https://i.ytimg.com/vi/mkJ6DVwDMjQ/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "mkJ6DVwDMjQ",
            "badge": "Watch Video"
          }
        ]
      },
      "bedaya": {
        "title": "Program Bedaya",
        "kicker": "TV Program",
        "description": "Selected work from Program Bedaya.",
        "cover": "https://i.ytimg.com/vi/3e-CpvJaMIg/hqdefault.jpg",
        "projects": [
          {
            "title": "Promo Bedaya",
            "subtitle": "Program Bedaya · TV Program Edit",
            "index": "BD01",
            "image": "https://i.ytimg.com/vi/3e-CpvJaMIg/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "3e-CpvJaMIg",
            "badge": "Watch Video"
          }
        ]
      },
      "my-guest-moataz-el-demerdash": {
        "title": "My Guest with Moataz El Demerdash",
        "kicker": "TV Program",
        "description": "Selected episodes and edits from My Guest with Moataz El Demerdash.",
        "cover": "https://i.ytimg.com/vi/_5EHAht5a1M/hqdefault.jpg",
        "projects": [
          {
            "title": "Nader Abbassy — My Guest with Moataz El Demerdash",
            "subtitle": "TV Program Edit",
            "index": "MG01",
            "image": "https://i.ytimg.com/vi/_5EHAht5a1M/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "_5EHAht5a1M",
            "badge": "Watch Video"
          },
          {
            "title": "Magdy Abdelghany — My Guest with Moataz El Demerdash",
            "subtitle": "TV Program Edit",
            "index": "MG02",
            "image": "https://i.ytimg.com/vi/_Sd8QUoXoaI/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "_Sd8QUoXoaI",
            "badge": "Watch Video"
          },
          {
            "title": "Hany Ramzy — My Guest with Moataz El Demerdash",
            "subtitle": "TV Program Edit",
            "index": "MG03",
            "image": "https://i.ytimg.com/vi/_7irVnrKMmM/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "_7irVnrKMmM",
            "badge": "Watch Video"
          },
          {
            "title": "Salah Abdallah — My Guest with Moataz El Demerdash",
            "subtitle": "TV Program Edit",
            "index": "MG04",
            "image": "https://i.ytimg.com/vi/_vUQ8quTX-w/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "_vUQ8quTX-w",
            "badge": "Watch Video"
          },
          {
            "title": "Amr Mostafa — My Guest with Moataz El Demerdash",
            "subtitle": "TV Program Edit",
            "index": "MG05",
            "image": "https://i.ytimg.com/vi/FwVPJqsdXBc/hqdefault.jpg",
            "imageFallback": "assets/on-e.webp",
            "youtube": "FwVPJqsdXBc",
            "badge": "Watch Video"
          }
        ]
      }
    }
  },
  "series": {
    "title": "Series",
    "kicker": "TV & Entertainment",
    "description": "Promos, songs and selected edits created for television series.",
    "cover": "assets/teatro-series-promo.webp",
    "projects": [
      {
        "title": "Promo — Teatro",
        "subtitle": "Series Promo · Video Editing",
        "index": "S01",
        "image": "assets/teatro-series-promo.webp",
        "video": "assets/teatro-series-promo.mp4",
        "badge": "Watch Promo"
      },
      {
        "title": "Abu Al-Arousa — Haytan Beitna",
        "subtitle": "Series Song · Video Editing",
        "index": "S02",
        "image": "https://i.ytimg.com/vi/hyYa8IUSJJc/hqdefault.jpg",
        "imageFallback": "assets/abu-el-arousa.webp",
        "youtube": "hyYa8IUSJJc",
        "badge": "Watch Video"
      },
      {
        "title": "Promo Series luebat alnisyan",
        "subtitle": "Series · Video Editing",
        "index": "S03",
        "image": "https://i.ytimg.com/vi/gLtyCZRuCCo/hqdefault.jpg",
        "imageFallback": "assets/teatro-series-promo.webp",
        "youtube": "gLtyCZRuCCo",
        "badge": "Watch Video"
      }
    ]
  },
  "video-clips": {
    "title": "Video Clips",
    "kicker": "Music Videos",
    "description": "Selected music videos and performance-led edits.",
    "cover": "https://i.ytimg.com/vi/eVf2BU9Tux4/hqdefault.jpg",
    "projects": [
      {
        "title": "Yasmine Niazy",
        "subtitle": "Music Video · Video Editing",
        "index": "VC01",
        "image": "https://i.ytimg.com/vi/eVf2BU9Tux4/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "youtube": "eVf2BU9Tux4",
        "badge": "Watch Video Clip"
      },
      {
        "title": "Promo Yasmin",
        "subtitle": "Music Video · Video Editing",
        "index": "VC02",
        "image": "https://i.ytimg.com/vi/yWmc4v00bFs/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "youtube": "yWmc4v00bFs",
        "badge": "Watch Video Clip"
      }
    ]
  },
  "institutional": {
    "title": "Institutional & Social Impact",
    "kicker": "Purpose-Driven Stories",
    "description": "Human-centered films and campaigns created for institutions and social-impact organizations.",
    "cover": "https://i.ytimg.com/vi/2KVyASYThgw/hqdefault.jpg",
    "projects": [
      {
        "title": "Hospital 57357 — Qowa Fi Alby",
        "subtitle": "Music Video · Video Editing",
        "index": "SI01",
        "image": "https://i.ytimg.com/vi/2KVyASYThgw/hqdefault.jpg",
        "imageFallback": "assets/hospital-57357.webp",
        "youtube": "2KVyASYThgw",
        "badge": "Watch Music Video"
      },
      {
        "title": "Medhat Saleh",
        "subtitle": "Music Video · Video Editing",
        "index": "SI02",
        "image": "https://i.ytimg.com/vi/SIndjl5ZIL0/hqdefault.jpg",
        "imageFallback": "assets/hospital-57357.webp",
        "youtube": "SIndjl5ZIL0",
        "badge": "Watch Music Video"
      }
    ]
  },
  "good-news": {
    "title": "Good News",
    "kicker": "Production & Entertainment",
    "description": "Selected editing work created for Good News.",
    "cover": "https://i.ytimg.com/vi/LLD5p0yP0fI/hqdefault.jpg",
    "projects": [
      {
        "title": "Showreel",
        "subtitle": "Good News · Video Editing",
        "index": "GN01",
        "image": "https://i.ytimg.com/vi/LLD5p0yP0fI/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "youtube": "LLD5p0yP0fI",
        "badge": "Watch Video"
      }
    ]
  },
  "on-e-channel": {
    "title": "ON E Channel",
    "kicker": "TV Channel",
    "description": "Selected channel promos, television edits and broadcast work for ON E Channel.",
    "cover": "https://i.ytimg.com/vi/8SzWYjluCpw/hqdefault.jpg",
    "projects": [
      {
        "title": "Promo — 7 Years Gouna",
        "subtitle": "ON E · TV Program Edit",
        "index": "ON01",
        "image": "https://i.ytimg.com/vi/8SzWYjluCpw/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "youtube": "8SzWYjluCpw",
        "badge": "Watch Video"
      },
      {
        "title": "Style Talk — Sherine Hamdy",
        "subtitle": "ON E · TV Program Edit",
        "index": "ON02",
        "image": "https://i.ytimg.com/vi/K6EtzANGU5k/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "youtube": "K6EtzANGU5k",
        "badge": "Watch Video"
      },
      {
        "title": "Lamees El Hadidy and the Creators of Al-Hashashin",
        "subtitle": "ON E · TV Program Edit",
        "index": "ON03",
        "image": "https://i.ytimg.com/vi/3UO9CNQP_mo/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "youtube": "3UO9CNQP_mo",
        "badge": "Watch Video"
      },
      {
        "title": "Naguib Sawiris — Interview on Egypt’s Investment Climate",
        "subtitle": "ON E · TV Program Edit",
        "index": "ON04",
        "image": "https://i.ytimg.com/vi/c7KL8K4AWGw/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "youtube": "c7KL8K4AWGw",
        "badge": "Watch Video"
      },
      {
        "title": "Disney On Ice — Cairo Stadium",
        "subtitle": "ON E · TV Program Edit",
        "index": "ON05",
        "image": "https://i.ytimg.com/vi/DmXmEbeisiA/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "youtube": "DmXmEbeisiA",
        "badge": "Watch Video"
      },
      {
        "title": "Interview with Egypt’s Minister of Investment",
        "subtitle": "ON E · TV Program Edit",
        "index": "ON06",
        "image": "https://i.ytimg.com/vi/V7OMgvsGFYQ/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "youtube": "V7OMgvsGFYQ",
        "badge": "Watch Video"
      },
      {
        "title": "El Gouna Film Festival — 7th Edition Opening",
        "subtitle": "ON E · TV Program Edit",
        "index": "ON07",
        "image": "https://i.ytimg.com/vi/nbpsCCxjxkM/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "youtube": "nbpsCCxjxkM",
        "badge": "Watch Video"
      },
      {
        "title": "El Gouna Film Festival — 5th Edition Opening",
        "subtitle": "ON E · TV Program Edit",
        "index": "ON08",
        "image": "https://i.ytimg.com/vi/4D7S9MiCszM/hqdefault.jpg",
        "imageFallback": "assets/on-e.webp",
        "youtube": "4D7S9MiCszM",
        "badge": "Watch Video"
      },
      {
        "title": "teaser Ahla Akla_01",
        "subtitle": "ON E · TV Program Edit",
        "index": "ON09",
        "image": "https://i.vimeocdn.com/video/1646579409-947332ad2494de7259602c8b4fb6f9d1340030577624ef9f7d206fa13c9b3145-d_295x166?region=us",
        "imageFallback": "assets/on-e.webp",
        "vimeo": "813971630",
        "badge": "Watch Video"
      },
      {
        "title": "teaser Ahla Akla_02",
        "subtitle": "ON E · TV Program Edit",
        "index": "ON10",
        "image": "https://i.vimeocdn.com/video/1646578954-300dbfe2ae582c20e6847b88699a8c5810033f3fc63a0d6ef04067a351bc4847-d_295x166?region=us",
        "imageFallback": "assets/on-e.webp",
        "vimeo": "813971433",
        "badge": "Watch Video"
      },
      {
        "title": "ON E — Fan Zone",
        "subtitle": "ON E · TV Program Edit",
        "index": "ON11",
        "image": "assets/on-e-11.jpg",
        "video": "assets/on-e-11.mp4",
        "badge": "Watch Video"
      }
    ]
  },
  "more-work": {
    "title": "More Selected Work",
    "kicker": "Additional Projects",
    "description": "A curated collection of additional edits across different formats and subjects.",
    "cover": "https://i.ytimg.com/vi/G1aMXgXTAog/hqdefault.jpg",
    "projects": [
      {
        "title": "FINAL ADS   AL HARAM",
        "subtitle": "Additional Project · Video Editing",
        "index": "MW01",
        "image": "https://i.ytimg.com/vi/G1aMXgXTAog/hqdefault.jpg",
        "youtube": "G1aMXgXTAog",
        "badge": "Watch Video"
      },
      {
        "title": "Reel 001",
        "subtitle": "Additional Project · Video Editing",
        "index": "MW02",
        "image": "https://i.ytimg.com/vi/fbrKZPloehw/hqdefault.jpg",
        "youtube": "fbrKZPloehw",
        "badge": "Watch Video"
      },
      {
        "title": "Rel 003",
        "subtitle": "Additional Project · Video Editing",
        "index": "MW03",
        "image": "https://i.ytimg.com/vi/T1VOBnWPwtE/hqdefault.jpg",
        "youtube": "T1VOBnWPwtE",
        "badge": "Watch Video"
      },
      {
        "title": "Reel 002",
        "subtitle": "Additional Project · Video Editing",
        "index": "MW04",
        "image": "https://i.ytimg.com/vi/0UY-_mTpUDA/hqdefault.jpg",
        "youtube": "0UY-_mTpUDA",
        "badge": "Watch Video"
      },
      {
        "title": "Gelod Final",
        "subtitle": "Additional Project · Video Editing",
        "index": "MW05",
        "image": "https://i.ytimg.com/vi/oIS4SghLtSs/hqdefault.jpg",
        "youtube": "oIS4SghLtSs",
        "badge": "Watch Video"
      },
      {
        "title": "Segad",
        "subtitle": "Additional Project · Video Editing",
        "index": "MW06",
        "image": "https://i.ytimg.com/vi/s72BulxLJgM/hqdefault.jpg",
        "youtube": "s72BulxLJgM",
        "badge": "Watch Video"
      },
      {
        "title": "Ganat Aksaswar",
        "subtitle": "Additional Project · Video Editing",
        "index": "MW07",
        "image": "https://i.ytimg.com/vi/5jaNOku5Tw0/hqdefault.jpg",
        "youtube": "5jaNOku5Tw0",
        "badge": "Watch Video"
      }
    ]
  },
  "sports": {
    "title": "Sports",
    "kicker": "Sports Content",
    "description": "Fast-paced sports edits, promotional content and club-focused storytelling.",
    "cover": "assets/al-ahly.webp",
    "projects": [
      {
        "title": "Al Ahly Club",
        "subtitle": "Sports Content · Video Collection",
        "index": "SP01",
        "image": "assets/al-ahly.webp",
        "collection": "al-ahly-club",
        "badge": "Open Collection"
      },
      {
        "title": "ON Sport",
        "subtitle": "Sports Channel · Selected Work",
        "index": "SP02",
        "image": "assets/client-logos/on-sport.png",
        "imageFallback": "assets/al-ahly.webp"
      }
    ],
    "collections": {
      "al-ahly-club": {
        "title": "Al Ahly Club",
        "kicker": "Sports Content",
        "description": "Selected Al Ahly Club edits and promotional sports content.",
        "cover": "assets/al-ahly.webp",
        "projects": [
          {
            "title": "Promo | FIBA African Basketball Championship",
            "subtitle": "Al Ahly Club · Sports Edit",
            "index": "AH01",
            "image": "https://i.ytimg.com/vi/N4uGPUETGb4/hqdefault.jpg",
            "imageFallback": "assets/al-ahly.webp",
            "youtube": "N4uGPUETGb4",
            "badge": "Watch Video"
          },
          {
            "title": "Opining FIBA | African Basketball Championship",
            "subtitle": "Al Ahly Club · Sports Edit",
            "index": "AH02",
            "image": "https://i.ytimg.com/vi/1eFghNwpODA/hqdefault.jpg",
            "imageFallback": "assets/al-ahly.webp",
            "youtube": "1eFghNwpODA",
            "badge": "Watch Video"
          }
        ]
      }
    }
  },
  "events": {
    "title": "Events",
    "kicker": "Event Coverage",
    "description": "Festival coverage, live-event storytelling and event-driven edits.",
    "cover": "assets/ciff.webp",
    "projects": [
      {
        "title": "Cairo International Film Festival",
        "subtitle": "Event Coverage · Video Collection",
        "index": "EV01",
        "image": "assets/ciff.webp",
        "collection": "ciff",
        "badge": "Open Collection"
      }
    ],
    "collections": {
      "ciff": {
        "title": "Cairo International Film Festival",
        "kicker": "Event Coverage",
        "description": "Selected Cairo International Film Festival edits and event coverage.",
        "cover": "assets/ciff.webp",
        "projects": [
          {
            "title": "Khan",
            "subtitle": "CIFF · Event Edit",
            "index": "CIFF01",
            "image": "https://i.ytimg.com/vi/8YHgTTQOKdo/hqdefault.jpg",
            "imageFallback": "assets/ciff.webp",
            "youtube": "8YHgTTQOKdo",
            "badge": "Watch Video"
          }
        ]
      }
    }
  },
  "ai-work": {
    "title": "AI Work",
    "kicker": "AI & Creative Technology",
    "description": "AI-generated visuals, creative experiments and cinematic AI work.",
    "cover": "assets/ai-work-01.jpg",
    "projects": [
      {
        "title": "AI Work 01",
        "subtitle": "AI Visuals · Creative Editing",
        "index": "AI01",
        "image": "assets/ai-work-01.jpg",
        "video": "assets/ai-work-01.mp4",
        "badge": "Watch Project"
      },
      {
        "title": "AI Work 02",
        "subtitle": "AI Visuals · Creative Editing",
        "index": "AI02",
        "image": "assets/ai-work-02.jpg",
        "video": "assets/ai-work-02.mp4",
        "badge": "Watch Project"
      },
      {
        "title": "AI Work 03",
        "subtitle": "AI Visuals · Creative Editing",
        "index": "AI03",
        "image": "assets/ai-work-03.jpg",
        "video": "assets/ai-work-03.mp4",
        "badge": "Watch Project"
      },
      {
        "title": "AI Work 04",
        "subtitle": "AI Visuals · Creative Editing",
        "index": "AI04",
        "image": "assets/ai-work-04.jpg",
        "video": "assets/ai-work-04.mp4",
        "badge": "Watch Project"
      },
      {
        "title": "AI Work 05",
        "subtitle": "AI Visuals · Creative Editing",
        "index": "AI05",
        "image": "assets/ai-work-05.jpg",
        "video": "assets/ai-work-05.mp4",
        "badge": "Watch Project"
      }
    ]
  }
};

function escapeHTML(value='') {
  return String(value).replace(/[&<>'"]/g, ch => ({
    '&':'&amp;',
    '<':'&lt;',
    '>':'&gt;',
    "'":'&#39;',
    '"':'&quot;'
  }[ch]));
}

function projectMarkup(project, categoryKey) {
  const formatClass = project.format === 'portrait' ? ' portrait-project' : '';
  const fallbackAttr = project.imageFallback
    ? ` data-fallback="${escapeHTML(project.imageFallback)}"`
    : '';

  if (project.collection) {
    const href = `index.html?category=${encodeURIComponent(categoryKey)}&collection=${encodeURIComponent(project.collection)}`;
    return `<a class="project-card reveal category-project-card project-link-card collection-card${formatClass}" href="${href}" aria-label="Open ${escapeHTML(project.title)} collection">
      <div class="project-image">
        <img src="${escapeHTML(project.image)}"${fallbackAttr} alt="${escapeHTML(project.title)}" loading="lazy">
        <span class="play-button collection-arrow" aria-hidden="true">→</span>
        <span class="available-badge">${escapeHTML(project.badge || 'Open Collection')}</span>
      </div>
      <div class="project-info">
        <div><h3>${escapeHTML(project.title)}</h3><p>${escapeHTML(project.subtitle)}</p></div>
        <span class="project-index">${escapeHTML(project.index)}</span>
      </div>
    </a>`;
  }

  const hasPlayable = Boolean(project.video || project.youtube || project.vimeo);
  let attrs = '';

  if (project.video) {
    attrs = ` data-video="${escapeHTML(project.video)}" data-poster="${escapeHTML(project.image)}" data-title="${escapeHTML(project.title)}" role="button" tabindex="0" aria-label="Play ${escapeHTML(project.title)}"`;
  } else if (project.youtube) {
    attrs = ` data-youtube="${escapeHTML(project.youtube)}" data-title="${escapeHTML(project.title)}" role="button" tabindex="0" aria-label="Play ${escapeHTML(project.title)}"`;
  } else if (project.vimeo) {
    attrs = ` data-vimeo="${escapeHTML(project.vimeo)}" data-title="${escapeHTML(project.title)}" role="button" tabindex="0" aria-label="Play ${escapeHTML(project.title)}"`;
  }

  return `<article class="project-card reveal category-project-card${hasPlayable ? ' project-video' : ''}${formatClass}"${attrs}>
    <div class="project-image">
      <img src="${escapeHTML(project.image)}"${fallbackAttr} alt="${escapeHTML(project.title)}" loading="lazy">
      <span class="play-button" aria-hidden="true">▶</span>
      <span class="available-badge">${escapeHTML(hasPlayable ? project.badge : 'Coming Soon')}</span>
    </div>
    <div class="project-info">
      <div><h3>${escapeHTML(project.title)}</h3><p>${escapeHTML(project.subtitle)}</p></div>
      <span class="project-index">${escapeHTML(project.index)}</span>
    </div>
  </article>`;
}

function renderCategoryPage(categoryKey, collectionKey) {
  if (!categoryKey && !collectionKey) return false;
  const category = Object.hasOwn(categoryData, categoryKey) ? categoryData[categoryKey] : null;
  const collection = collectionKey && category?.collections && Object.hasOwn(category.collections, collectionKey)
    ? category.collections[collectionKey] : null;
  const invalidRoute = !category || Boolean(collectionKey && !collection);
  const pageData = invalidRoute ? {
    title:'Work not found', kicker:'Portfolio',
    description:'This category or collection is unavailable. Choose a work category below.',
    cover:'assets/showreel.webp', projects:[]
  } : collection || category;
  const isCollection = !invalidRoute && Boolean(collection);

  document.body.classList.add('category-page');
  document.body.classList.toggle('collection-page', isCollection);
  document.title = `${pageData.title} — Sayed Abdallah`;

  const main = document.querySelector('main');
  const projects = pageData.projects?.length
    ? pageData.projects.map(project => projectMarkup(project, categoryKey)).join('')
    : invalidRoute
      ? `<div class="empty-state reveal"><h3>Choose another collection</h3><a class="button button-outline" href="index.html#categories">All Work Categories</a></div>`
      : `<div class="empty-state reveal"><span>◇</span><h3>Projects are being prepared</h3><p>Selected work will be added here.</p><a class="button button-outline" href="index.html#contact">Discuss a Project</a></div>`;

  const gridClass = pageData.layout === 'portrait'
    ? 'portrait-project-grid'
    : 'category-project-grid';

  const backLink = isCollection
    ? `<a class="back-link" href="index.html?category=${encodeURIComponent(categoryKey)}">← Back to ${escapeHTML(category.title)}</a>`
    : `<a class="back-link" href="index.html#categories">← All Work Categories</a>`;

  const related = isCollection
    ? `<a href="index.html?category=${encodeURIComponent(categoryKey)}">${escapeHTML(category.title)}<span>←</span></a>`
    : Object.entries(categoryData)
        .filter(([id]) => id !== categoryKey)
        .map(([id,item]) => `<a href="index.html?category=${id}">${escapeHTML(item.title)}<span>→</span></a>`)
        .join('');

  main.innerHTML = `<section class="portfolio-page-hero" style="--page-cover:url('${escapeHTML(pageData.cover)}')">
      <div class="page-hero-overlay"></div>
      <div class="page-hero-content reveal">
        ${backLink}
        <p class="kicker">${escapeHTML(pageData.kicker)}</p>
        <h1>${escapeHTML(pageData.title)}</h1>
        <p>${escapeHTML(pageData.description)}</p>
      </div>
    </section>
    <section class="section page-projects" id="projects">
      <div class="section-heading reveal">
        <div>
          <p class="kicker">${isCollection ? 'Video Collection' : 'Selected Work'}</p>
          <h2>${isCollection ? 'Episodes & Promos' : 'Projects'}</h2>
        </div>
      </div>
      <div class="promo-grid ${gridClass}">${projects}</div>
    </section>
    <section class="section explore-more">
      <p class="kicker reveal">${isCollection ? 'Return' : 'Explore More'}</p>
      <div class="category-nav reveal">${related}</div>
    </section>`;

  const nav = document.querySelector('.main-nav');
  if (nav) {
    nav.innerHTML = '<a href="index.html">Home</a><a class="active" href="index.html#categories">Work</a><a href="index.html#about">About</a><a href="index.html#contact">Contact</a>';
  }

  document.querySelectorAll('.portfolio-sidebar a[href^="#"]').forEach(link => {
    link.setAttribute('href', `index.html${link.getAttribute('href')}`);
  });

  const cta = document.querySelector('.header-cta');
  if (cta) cta.href = 'index.html#showreel';

  return true;
}

// Normalize old bookmarks before rendering or attaching UI behavior.
const route = new URL(location.href);
let requestedCategory = route.searchParams.get('category');
let requestedCollection = route.searchParams.get('collection');
if (requestedCategory === 'sports-events') {
  if (requestedCollection === 'ciff') requestedCategory = 'events';
  else if (requestedCollection === 'al-ahly' || requestedCollection === 'al-ahly-club') {
    requestedCategory = 'sports';
    requestedCollection = 'al-ahly-club';
  } else if (!requestedCollection) {
    // A combined category bookmark cannot tell us which project was intended.
    requestedCategory = null;
    route.hash = '#categories';
  }
}
if (requestedCategory === 'sports' && requestedCollection === 'al-ahly') requestedCollection = 'al-ahly-club';
if (requestedCategory === 'motion-graphics') requestedCategory = 'ai-work';
if (requestedCategory === 'tv-programs' && requestedCollection === 'on-e') {
  requestedCategory = 'on-e-channel';
  requestedCollection = null;
}
if (requestedCategory) route.searchParams.set('category', requestedCategory);
else route.searchParams.delete('category');
if (requestedCollection) route.searchParams.set('collection', requestedCollection);
else route.searchParams.delete('collection');
if (route.href !== location.href) history.replaceState(null, '', route.pathname + route.search + route.hash);
renderCategoryPage(requestedCategory, requestedCollection);

// Capture errors from current and future cards; late collection renders remain usable.
document.addEventListener('error', event => {
  const image = event.target;
  if (!image.matches?.('img[data-fallback]')) return;
  const fallback = image.dataset.fallback;
  if (fallback) {
    delete image.dataset.fallback;
    image.src = fallback;
  }
}, true);

const header = document.querySelector('.site-header');
const menuButton = document.querySelector('.menu-toggle');
const nav = document.querySelector('.main-nav');
const toast = document.querySelector('.toast');

if (header) {
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 24);
  });
}

if (menuButton && nav) {
  menuButton.addEventListener('click', () => {
    const open = !nav.classList.contains('open');
    nav.classList.toggle('open', open);
    menuButton.classList.toggle('active', open);
    menuButton.setAttribute('aria-expanded', String(open));
    document.body.classList.toggle('menu-open', open);
  });

  nav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('open');
      menuButton.classList.remove('active');
      menuButton.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('menu-open');
    });
  });
}

if ('IntersectionObserver' in window) {
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: .12 });

  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

  const sections = [...document.querySelectorAll('main section[id]')];
  const localNavLinks = [...document.querySelectorAll('.main-nav a[href^="#"]')];

  if (sections.length && localNavLinks.length) {
    const sectionObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          localNavLinks.forEach(link => {
            link.classList.toggle('active', link.getAttribute('href') === `#${entry.target.id}`);
          });
        }
      });
    }, { rootMargin: '-35% 0px -55% 0px' });

    sections.forEach(section => sectionObserver.observe(section));
  }
} else {
  document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
}

const videoModal = document.getElementById('video-modal');
const videoPlayer = document.getElementById('project-video-player');
let youtubePlayer = document.getElementById('youtube-video-player');
if (!youtubePlayer && videoModal) {
  youtubePlayer = document.createElement('iframe');
  youtubePlayer.id = 'youtube-video-player';
  youtubePlayer.title = 'YouTube video player';
  youtubePlayer.src = 'about:blank';
  youtubePlayer.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
  youtubePlayer.allowFullscreen = true;
  youtubePlayer.referrerPolicy = 'strict-origin-when-cross-origin';
  youtubePlayer.hidden = true;
  videoModal.querySelector('.video-modal-inner')?.appendChild(youtubePlayer);
}
const videoTitle = document.getElementById('video-modal-title');
const videoClose = document.querySelector('.video-modal-close');
let lastTrigger = null;

function resetModalPlayers() {
  if (videoPlayer) {
    videoPlayer.pause();
    videoPlayer.removeAttribute('src');
    videoPlayer.removeAttribute('poster');
    videoPlayer.load();
    videoPlayer.hidden = true;
  }

  if (youtubePlayer) {
    youtubePlayer.src = 'about:blank';
    youtubePlayer.hidden = true;
  }
}

function openProjectVideo(card) {
  if (!videoModal || !videoTitle || (!card.dataset.video && !card.dataset.youtube && !card.dataset.vimeo)) return;

  lastTrigger = card;
  resetModalPlayers();
  videoModal.classList.remove('portrait-video', 'youtube-video');
  videoTitle.textContent = card.dataset.title || 'Project Video';

  if (card.dataset.youtube && youtubePlayer) {
    const videoId = encodeURIComponent(card.dataset.youtube);
    youtubePlayer.src = `https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&rel=0&playsinline=1`;
    youtubePlayer.hidden = false;
    videoModal.classList.add('youtube-video');
  } else if (card.dataset.vimeo && youtubePlayer) {
    youtubePlayer.src = `https://player.vimeo.com/video/${encodeURIComponent(card.dataset.vimeo)}?autoplay=1&title=0&byline=0&portrait=0`;
    youtubePlayer.hidden = false;
    videoModal.classList.add('youtube-video');
  } else if (card.dataset.video && videoPlayer) {
    videoPlayer.src = card.dataset.video;
    videoPlayer.poster = card.dataset.poster || '';
    videoPlayer.hidden = false;
  }

  videoModal.classList.add('open');
  videoModal.setAttribute('aria-hidden', 'false');
  document.body.classList.add('video-open');
  videoClose?.focus();
}

function closeProjectVideo() {
  if (!videoModal) return;

  resetModalPlayers();
  videoModal.classList.remove('open', 'portrait-video', 'youtube-video');
  videoModal.setAttribute('aria-hidden', 'true');
  document.body.classList.remove('video-open');
  lastTrigger?.focus();
}

videoPlayer?.addEventListener('loadedmetadata', () => {
  videoModal?.classList.toggle('portrait-video', videoPlayer.videoHeight > videoPlayer.videoWidth);
});

function activateProject(event) {
  const card = event.target.closest?.('.project-card, .selected-card');
  if (!card) return;
  if (event.type === 'keydown' && event.key !== 'Enter' && event.key !== ' ') return;
  if (card.dataset.video || card.dataset.youtube || card.dataset.vimeo) {
    event.preventDefault();
    openProjectVideo(card);
  } else if (!card.matches('a') && toast) {
    toast.classList.add('show');
    clearTimeout(window.__toastTimer);
    window.__toastTimer = setTimeout(() => toast.classList.remove('show'), 2600);
  }
}
document.addEventListener('click', activateProject);
document.addEventListener('keydown', activateProject);

videoClose?.addEventListener('click', closeProjectVideo);
videoModal?.addEventListener('click', event => {
  if (event.target === videoModal) closeProjectVideo();
});

document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && videoModal?.classList.contains('open')) {
    closeProjectVideo();
  }
});

const year = document.getElementById('year');
if (year) year.textContent = new Date().getFullYear();
