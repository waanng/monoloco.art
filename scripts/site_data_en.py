"""Edited English copy. Slugs, media IDs and artwork stay shared with Chinese."""
from copy import deepcopy
from family_content import FAMILY_SELECTION, WORKSHOP_PHOTOS, FAMILY_ALT

PROJECT_COPY = {'four-doors': {'title': 'Four Doors',
                'subtitle': 'A study in doorways',
                'author': 'monoloco archive',
                'kind': 'Photography',
                'intro': 'Four doorways, one place. Seen together, their differences become as striking as '
                         'the details they share. Each set offers a small portrait of a place through its '
                         'entrances.'},
 'qianmo': {'title': 'Qianmo',
            'subtitle': 'Drawing a place, marking a moment',
            'author': 'waanng',
            'kind': 'Travel sketches / Maps / Postmarks',
            'intro': 'Wherever I travel, I stop to draw. A sketch and a map share the page; a stamp, '
                     'postmarked locally that day, fixes it to a time and place. Each page becomes a record '
                     'of where I was and what caught my eye.',
            'quote': 'A place on the map. A moment on the page.',
            'paragraphs': ['The sketch captures an impression; the map gives it a location. A stamp and a '
                           'dated postmark add another kind of record. Photographed against the scene, the '
                           'open sketchbook brings the drawing back into the world that prompted it.',
                           'Qianmo is a Chinese word for the paths that crisscross fields. For me, '
                           'those crossings suggest other meeting points: time and place, intuition and '
                           'reason. A drawing made in the moment sits beside the precision of a map and a '
                           'date. Together, they offer different ways of remembering the same journey.'],
            'captions': ['Travel sketch 01',
                         'Travel sketch 02',
                         'Travel sketch 03',
                         'Travel sketch 04',
                         'Travel sketch 05',
                         'Travel sketch 06',
                         'Travel sketch 07',
                         'Travel sketch 08',
                         'Travel sketch 09',
                         'Travel sketch 10',
                         'Travel sketch 11',
                         'Travel sketch 12',
                         'Travel sketch 13',
                         'Travel sketch 14',
                         'Travel sketch 15',
                         'Travel sketch 16',
                         'Travel sketch 17',
                         'Travel sketch 18',
                         'Travel sketch 19'],
            'source_note': 'Drawings and photographs by waanng. Text based on the artist’s account.',
            'related_label': 'Make a notebook for your own travels'},
 'planters-notes': {'title': 'A Gardener’s Notes',
                    'subtitle': 'Getting to know the soil',
                    'author': 'LZ',
                    'kind': 'Photography / Gardening',
                    'intro': 'Growing things begins with a packet of seeds—and soon leads to questions about '
                             'soil, insects and compost. These photographs follow the small discoveries, '
                             'surprises and setbacks of tending a garden.',
                    'quote': 'Coffee grounds, eggshells, a little patience.',
                    'paragraphs': ['I started by trying different seeds. The results were not always what I '
                                   'had hoped for, but pests and plant diseases gave me more to investigate. '
                                   'What do earthworms eat? What makes good soil?',
                                   'The photographs grew out of paying attention, day after day. Kitchen '
                                   'scraps turn into compost; seedlings take root. Gardening offers a '
                                   'practical way to feel more connected to the ground beneath us.'],
                    'captions': ['A harvest begins in the soil.',
                                 'A seedling breaks through.',
                                 'A sign with a simple request: please don’t take the soil.',
                                 'A little growth on the windowsill.',
                                 'Beyond the vegetable patch.',
                                 'A closer look.']},
 'five-kilometers': {'title': 'Five Kilometres',
                     'subtitle': 'A closer look at familiar places',
                     'author': 'KASA',
                     'kind': 'Urban photography',
                     'intro': 'How much do we notice within five kilometres of home? Starting with familiar '
                              'surroundings, this series looks at the roads, buildings, rooms and people '
                              'that shape daily life in the city.',
                     'quote': 'Look again at the places you know.',
                     'paragraphs': ['As the city grows, our daily routes change. Familiar streets give way '
                                    'to new spaces, and the places we thought we knew begin to look '
                                    'different.',
                                    'A window, a reading room, a doorway: these photographs pause over the '
                                    'light and quiet of places we might otherwise pass without a second '
                                    'glance.'],
                     'captions': ['The city, seen from above.',
                                  'A book by the window.',
                                  'A quiet moment.',
                                  'Absorbed in a book.',
                                  'Inside the building.',
                                  'At the entrance.',
                                  'Branches beyond the glass.',
                                  'An ordinary day in the reading room.',
                                  'A seat in the light.',
                                  'A room for art and everyday life.',
                                  'A life glimpsed through a room.']},
 'traveler': {'title': 'The Traveller',
              'subtitle': 'What stays with us',
              'author': 'LZ',
              'kind': 'Travel photography',
              'intro': 'A street corner, a station, a cat, a ripple on the water. The things we remember '
                       'from a trip are not always its landmarks. These photographs return to the smaller '
                       'encounters that make a place stay with us.',
              'quote': 'Something of being there stays in the photograph.',
              'paragraphs': ['Travel memories rarely arrive in order. One place comes back as a face outside '
                             'a shop; another as a cat in an alley or a few minutes spent beside the water.',
                             'These photographs leave the journey open-ended. Scenes from different places '
                             'sit alongside one another, connected by the act of looking.'],
              'captions': ['A view from where I sit.',
                           'At the crossing.',
                           'Outside the shop.',
                           'A cat looks back.',
                           'Ripples on the water.',
                           'Down another alley.',
                           'At the platform.',
                           'A crossing along the way.']},
 'journey-notes': {'title': 'The Three of Us',
                   'subtitle': 'Our family, on the road',
                   'author': 'waanng',
                   'kind': 'Photography / Travel maps',
                   'intro': 'The Three of Us is a family album made along the way: a walk through a new '
                            'city, a shared meal, a place to sit, a handful of balloons. Photographs '
                            'remember our time together; hand-drawn maps trace the journeys.',
                   'quote': 'A long road ahead. Each other to lean on.',
                   'paragraphs': ['We keep going. Sometimes we run ahead; sometimes we stop to rest. We look '
                                  'at each other and smile. There is a long road ahead, and we have each '
                                  'other to lean on.',
                                  'Coasts and campuses, parks and backstreets, bookshops and galleries: the '
                                  'setting changes, but we are still us. Two people in front of the camera, '
                                  'one behind it. The three of us.',
                                  'The maps show where we went. The photographs remember what it was like to '
                                  'be there together. This is less a list of destinations than an album of '
                                  'the moments in between.'],
                   'source_note': 'Photographs and travel maps from The Three of Us, a family album by '
                                  'waanng. The opening passage is adapted from its preface.',
                   'related_label': 'Make a notebook for your travels'}}

WORKSHOP_COPY = {'handmade-books': {'title': 'Bookbinding Workshop',
                    'subtitle': 'Make a notebook. Make it yours.',
                    'tag': 'Reclaimed paper / Bookbinding / Journalling',
                    'intro': 'Give saved wrapping paper and other everyday materials a second life. Turn '
                             'loose sheets into a small notebook, ready for your photographs, sketches and '
                             'notes.',
                    'stages': [('01',
                                'Start with what you have',
                                'Look for paper and packaging you would like to use again. Choose a cover '
                                'and gather pages for a notebook you can take anywhere.'),
                               ('02',
                                'Put the pages together',
                                'Try a stitched, ring-bound or accordion book. We’ll announce the binding '
                                'method and materials for each session in advance.'),
                               ('03',
                                'Make the first mark',
                                'A photograph, a line on a map, a few words: start anywhere. You don’t need '
                                'to be able to draw to keep a notebook.')],
                    'outcome': 'Leave with a notebook you’ve made yourself, and plenty of ideas for filling '
                               'it.',
                    'preparation': 'Save any paper, packaging or photographs you’d like to use. We’ll share '
                                   'a materials list when each session is announced.'},
 'cyanotype': {'title': 'Cyanotype Workshop',
               'subtitle': 'Make a print with sunlight.',
               'tag': 'Sunlight / Plants / Photography',
               'intro': 'Cyanotype uses light-sensitive paper to make distinctive blue prints. Arrange '
                        'leaves or other objects on the surface, expose it to sunlight, then wash the paper '
                        'to reveal your image.',
               'stages': [('01',
                           'Discover cyanotype',
                           'Find out how light-sensitive paper produces the process’s characteristic blue.'),
                          ('02',
                           'Arrange your image',
                           'Choose your objects and play with shapes, shadows and the spaces between them '
                           'before exposing the paper.'),
                          ('03',
                           'Reveal the print',
                           'Wash the paper and watch the image emerge. Each print is a little experiment in '
                           'light and timing.')],
               'outcome': 'Make a cyanotype print and discover a hands-on approach to photography.',
               'preparation': 'Materials and activities will vary by session. We’ll provide details in '
                              'advance and guide you through the process on the day.'},
 'film-developing': {'title': 'Film Developing Workshop',
                     'subtitle': 'From the shutter to the negative.',
                     'tag': 'Black-and-white film / Darkroom processes',
                     'intro': 'What happens between taking a photograph and seeing it? This workshop will '
                              'introduce black-and-white film development, following the steps that turn an '
                              'exposed roll into negatives.',
                     'stages': [('01',
                                 'Get to know film',
                                 'Explore how a camera records an image on film and what happens after the '
                                 'shutter closes.'),
                                ('02',
                                 'Inside the developing process',
                                 'Learn about the equipment and main stages of black-and-white development. '
                                 'We’ll explain the hands-on activities when each session is announced.'),
                                ('03',
                                 'Read the negative',
                                 'Look at the developed film and consider how it becomes a photograph. '
                                 'Scanning or printing may be included, depending on the session.')],
                     'outcome': 'Learn what happens to a roll of film after it leaves the camera. Hands-on '
                                'activities and take-home materials will be confirmed for each session.',
                     'preparation': 'We’re still planning this workshop. We’ll announce who it’s for, what '
                                    'to bring and where it will take place when the details are confirmed.'}}

OBJECT_COPY = {'vinyl-notebook': {'title': 'Vinyl Travel Notebook',
                    'subtitle': 'A travel notebook inspired by vinyl records',
                    'kind': 'Notebook design',
                    'intro': 'A record player becomes the starting point for a travel notebook. Turntable '
                             'graphics, urban sketches and space for personal notes bring music and travel '
                             'together on the page.',
                    'sections': [('vinyl-cover',
                                  '01 / COVER',
                                  'A record player, reimagined',
                                  'The turntable, tonearm and controls become a simple graphic composition. '
                                  'BEYOND THE NOTES connects the notes we hear with the notes we write. '
                                  'Shown here in a dark coffee-brown colourway.'),
                                 ('vinyl-label',
                                  '02 / INSIDE COVER',
                                  'This one belongs to…',
                                  'A record’s centre label becomes a place for the owner’s name, notebook '
                                  'number and dates. The design sets the scene; the person using it writes '
                                  'the rest.')],
                    'details': [('Inspired by', 'Music, travel and urban sketches'),
                                ('Design includes',
                                 'Cover, inside cover, seven city inserts and a paper wrap'),
                                ('On this page', 'Design proposal in dark coffee brown')],
                    'closing': 'For the journey you’re on, and the one still to come.'},
 'ucas-cup': {'title': 'UCAS Campus Cup',
              'subtitle': 'A little of campus, taken home',
              'kind': 'Cup & packaging design',
              'intro': 'A hand-painted campus panorama becomes a cup and its packaging. The design draws on '
                       'the Yuquanlu, Zhongguancun and Yanqihu campuses of the University of Chinese Academy '
                       'of Sciences (UCAS).',
              'sections': [('ucas-scroll',
                            '01 / THE STARTING POINT',
                            'Back on campus',
                            'Years after graduating, waanng returned to three UCAS campuses to paint their '
                            'buildings and grounds as a long, continuous panorama. That return became the '
                            'starting point for the cup.'),
                           ('ucas-sketch',
                            '02 / FROM PAPER TO CUP',
                            'Finding the right lines',
                            'Selected buildings are redrawn as a set of illustrations, taking them from the '
                            'continuous panorama to the curved surface of a cup.'),
                           ('ucas-cup',
                            '03 / THE CUP',
                            'A familiar view, every day',
                            'Building illustrations and text bring familiar places into daily use. The '
                            'proposal uses recycled coffee grounds as a material for the cup.'),
                           ('ucas-package',
                            '04 / THE PACKAGING',
                            'Three campuses, one skyline',
                            'The packaging brings buildings from all three campuses into a continuous, '
                            'geometric skyline—a new way to unfold the panorama. Shown here is a detail of '
                            'the packaging design.')],
              'details': [('Based on', 'waanng’s campus panorama and architectural sketches'),
                          ('Design includes', 'Cup illustrations and packaging'),
                          ('On this page', 'Graphic design proposal for a campus gift cup')],
              'closing': 'A reminder of campus, with every cup.'}}

MEMBER_COPY = {'lz': {'name': 'LZ',
        'line': 'Film, travel and things that grow',
        'bio': 'LZ comes from a media background and loves exploring a place through its everyday '
               'life—especially its markets. Film photography is a way to remember those encounters. Closer '
               'to home, gardening, composting and permaculture feed a growing interest in the land and how '
               'we care for it.'},
 'kasa': {'name': 'KASA',
          'line': 'A camera, a bicycle, an eye for the city',
          'bio': 'KASA is a photographer and keen cyclist, attentive to the frame and to the city beyond it. '
                 'The work follows changing urban spaces and scenes along the road, with an eye for the '
                 'humour in everyday life.'},
 'wangan': {'name': 'waanng',
            'line': 'Walking, looking, drawing',
            'bio': 'A self-taught urban sketcher, waanng draws whatever catches the eye along the way. '
                   'Sketches, photographs and handmade notebooks become a record of everyday life and family '
                   'travels. Some drawings go on to become objects people can use.'}}

PROJECT_COPY['journey-notes']['captions'] = [en for key,file,zh,en in FAMILY_SELECTION]

DOOR_TITLES = ['Oxford Street, Boston','Stanford University','289 Art Park, Guangzhou','Rice University','University of Washington','University of Utah','Freedom Trail, Boston','University of Pennsylvania','SMU','Baylor University','Zhijiang campus, Zhejiang University','Xiangshan campus, China Academy of Art']

def localized_content(projects,workshops,objects,members,doors):
    projects,workshops,objects,members,doors=deepcopy((projects,workshops,objects,members,doors))
    for p in projects:
        copy=deepcopy(PROJECT_COPY[p['slug']])
        captions=copy.pop('captions',None)
        related=copy.pop('related_label',None)
        p.update(copy)
        if captions is not None:
            assert len(captions)==len(p['media'])
            p['media']=[(item[0],caption) for item,caption in zip(p['media'],captions)]
        if related:p['related']=(p['related'][0],related)
    for w in workshops:w.update(deepcopy(WORKSHOP_COPY[w['slug']]))
    for o in objects:o.update(deepcopy(OBJECT_COPY[o['slug']]))
    for m in members:m.update(deepcopy(MEMBER_COPY[m['image']]))
    for d,title in zip(doors,DOOR_TITLES):
        d['titleZh']=title
        d['altZh']=f'Four doorways at {title}, arranged as a four-part photograph.'
    return projects,workshops,objects,members,doors

ALT = {
 'lz':'Black-and-white portrait of LZ.', 'kasa':'KASA with a large-format camera.', 'wangan':'Portrait of waanng.',
 'plant-bananas':'Bunches of bananas forming a black-and-white pattern.','plant-soil':'A young seedling emerging from the soil.','plant-sign':'A sign reading “No stealing soil” beside a planter.','plant-light':'A seedling in a glass beside a window.','plant-pigs':'Pigs behind a railing.','plant-detail':'A close view of fine netting and a plant.',
 'travel-window':'Feet in the foreground, with a view stretching beyond them.','travel-street':'People and passing vehicles at a street crossing.','travel-shop':'A person and objects outside a shop.','travel-cat':'A cat looking out from a window.','travel-water':'A waterbird and ripples on the surface.','travel-lane':'Signs hanging in a narrow alley.','travel-station':'A train beside a station platform.','travel-bridge':'A person crossing a wooden walkway.',
 'five-city':'Rooftops and a city skyline seen from above.','five-window':'A book and light by a window, photographed on film.','five-reader':'A person reading beside a window.','five-portrait':'A close view of a reader and the pages of a book.','five-building':'An interior courtyard with surrounding galleries.','five-door':'An entrance marked D-22.','five-branches':'Branches seen through a window.','five-library':'Lights, tables and chairs in a reading room.','five-seat':'A seated figure beside a window.','five-studio':'A room filled with artworks and books.','five-room':'A room with plants, pictures and furniture.',
 'film-camera':'A hand-drawn diagram of a Mamiya C220 twin-lens camera, with original Chinese annotations.',
 'journey-map':'A hand-drawn route map from a family journey.','journey-list':'A handwritten list of places visited.','journey-road':'An adult and a child walking past a building.','journey-trees':'A path beneath trees.','journey-texas':'A hand-drawn map of a journey through Texas.','journey-family':'A family posing together in a doorway during a trip.','journey-west':'A hand-drawn route along Highway 1.','journey-house':'A house at a street corner encountered during a journey.','journey-east':'A hand-drawn map of an East Coast journey.','journey-campus':'A child climbing steps on a university campus.','journey-bookshop':'A family travel photograph outside a bookshop.','journey-balloon':'Family members photographed beside balloons.',
 'notebooks':'Nine small handmade notebooks with different covers and bindings.','notebook-map':'A route drawn across the pages of a handmade notebook.','notebook-writing':'Handwritten notes in a small notebook.','notebook-coffee':'Writing, sketches and collected stickers inside a notebook.','notebook-photo':'Two photographs attached inside a notebook.',
 'vinyl-cover':'A notebook cover design with a turntable graphic and the words BEYOND THE NOTES.','vinyl-label':'An opening page based on a record label, with space for a name and dates.','vinyl-band':'A detail of the paper band with a route map and a travel theme.',
 'ucas-scroll':'A painted scroll combining campus buildings and handwritten inscriptions.','ucas-sketch':'Four groups of campus buildings drawn in line.','ucas-package':'A detail of the packaging graphics: a geometric campus skyline.','ucas-cup':'Flat front and back graphic studies for the UCAS gift cup.',
 'cyanotype-print-1':'A photographic sequence showing plant shapes emerging in a cyanotype print.',
 'cyanotype-process-1':'Hand-drawn cyanotype notes: preparing the coating and applying it evenly.',
 'cyanotype-process-2':'Hand-drawn cyanotype notes: coating the paper and drying it away from light.',
 'cyanotype-process-3':'Hand-drawn cyanotype notes: arranging objects, exposing the print and washing it.',
 'binding-process-1':'A hand-drawn stitched binding sequence: cut paper, make holes and sew the pages.',
 'binding-process-2':'A hand-drawn ring-binding sequence: trim paper, punch holes and insert rings.',
 'binding-process-3':'A hand-drawn accordion book: score the folds and fold the strip between covers.'
}
for i,city in enumerate(['Liverpool','Amsterdam','Berlin','Prague','Vienna','Milan','Paris'],1):
    ALT[f'vinyl-city-{i}']=f'An urban sketch of {city} arranged within a record-shaped notebook insert.'
for i in range(1,20):
    ALT[f'qianmo-{i:02d}']=f'Qianmo field photograph {i:02d}: an open sketchbook held against the scene, with drawings, maps or stamps and postmarks on its pages.'

# Supplied colour originals replace magazine reproductions.
ALT.update({key:en for key,(file,zh,en) in WORKSHOP_PHOTOS.items()})
ALT.update({key:en for key,(zh,en) in FAMILY_ALT.items()})
