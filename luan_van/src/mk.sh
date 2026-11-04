set -e
S=/tmp/claude-0/-home-user-ebs-ecm/23ed5344-f225-5ffd-9c91-08b42592134c/scratchpad; SK=/root/.claude/skills/synced/f32ec81f-3c5f-4173-957a-151cf2b45b68_c35a6f55-1b4a-46ce-89e7-57872e4164c2/docx
cd $S
build(){ rm -rf fu && cp -r cover/u fu && python3 work/build_full.py fu/word/document.xml work "$1" >/dev/null && (cd fu && rm -f ../full.docx && zip -qXr ../full.docx .) && rm -rf pf && mkdir pf && python $SK/scripts/office/soffice.py --headless --convert-to pdf --outdir pf full.docx >/dev/null 2>&1; }
build '{}'; P=$(python3 work/pages.py pf/full.pdf work/toc.json | tail -1)
build "$P"; P2=$(python3 work/pages.py pf/full.pdf work/toc.json | tail -1)
[ "$P" = "$P2" ] && echo stable || echo CHANGED
pdfinfo pf/full.pdf | grep Pages; python $SK/scripts/office/validate.py full.docx 2>&1 | tail -1
