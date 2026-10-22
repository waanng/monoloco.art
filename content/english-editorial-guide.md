# monoloco English editorial notes

The English site is an edition for English-speaking visitors, rather than a sentence-by-sentence translation. Its voice is clear, observant and informal: an artist speaking to a curious visitor. Keep the Chinese site’s facts, authorship and intentions; allow English sentences and paragraph order to take their own shape.

- Lead with what the reader is looking at or can do. Prefer concrete language such as “Make a print with sunlight” to translated abstractions.
- Give each page its own voice. Project texts explain the work; workshops address participants directly; The Three of Us reads as a personal family album.
- Keep headings and image captions brief. Avoid repeating the introduction in the subtitle, or the caption in the alt text. Alt text describes the image; captions can add a thought.
- Use British English consistently: colour, travelling, kilometres, neighbourhood, journalling. Preserve words printed in artwork, account handles and official names.
- Retain Qianmo as the title and explain its meaning in plain English. Expand UCAS on first mention. Give unfamiliar cultural terms enough context to follow the work.
- Use “we” for the collective and the family’s shared experiences, “I” for an artist’s own account, and member names in third-person biographies. Keep those voices distinct.
- Describe proposals as proposals. Workshops have no confirmed dates yet; do not imply that booking is open. Do not invent locations, personal anecdotes, qualifications or contact details.
- Read each page as a standalone piece of English, then compare it with the Chinese source for changes in meaning. Remove unnecessary explanations and repeated words such as “record”, “moment” and “everyday”, without treating them as banned vocabulary.

## Editing and release

Project descriptions, workshop details and biographies live in `scripts/site_data_en.py`. Shared interface and page copy live in `scripts/site_i18n.py`. Paired family captions live in `scripts/family_content.py`. Preserve Chinese strings, shared image IDs and page addresses when editing English.

Build both languages and run the site checks. Verify that Chinese output is unchanged and that longer English headings fit on a phone. Test language links and the image viewer before publishing. This is an editorial guide, not a claim of review by a native-speaking human editor.

## Agreed terms and homepage line

Use **Products** for the 文创作品 section, including navigation, page titles, breadcrumbs and section headings. Use **product design** for the discipline; keep “objects” where it refers to physical items, such as leaves placed on cyanotype paper. Keep the existing `/objects/` addresses so shared links remain valid.

Use **urban sketches** and **urban sketching** for 城市速写, with **urban sketcher** for the person. The brand phrase is **Art in Everyday Life** (capitalisation may follow the page’s typographic style). The homepage invitation is **Find joy in the everyday. / Make something together.** It should suggest pleasure and curiosity, rather than an instruction to analyse or scrutinise daily life.
