import MarkdownIt from 'markdown-it';
import hljs from 'highlight.js';

const md = new MarkdownIt({
  html: true,
  highlight: (str: string, lang: string): string => {
    let result;
    if (lang && hljs.getLanguage(lang)) {
      try {
        result = hljs.highlight(str, {
          language: lang,
          ignoreIllegals: true,
        });
      } catch (_e) {
        result = hljs.highlightAuto(str);
      }
    } else {
      result = hljs.highlightAuto(str);
    }
    return (
      '<pre class="hljs my-4 p-4 overflow-scroll rounded-lg"><code>' +
      result.value +
      '</code></pre>'
    );
  },
});

function removeFirstPTag(md: MarkdownIt): void {
  md.core.ruler.push('remove_first_p_tag', (state) => {
    const tokens = state.tokens;
    const pTagStartIndex = tokens.findIndex(
      (token) => token.type === 'paragraph_open'
    );
    const pTagEndIndex = tokens.findIndex(
      (token) => token.type === 'paragraph_close'
    );

    if (pTagStartIndex !== -1 && pTagEndIndex !== -1) {
      tokens.splice(pTagEndIndex, 1);
      tokens.splice(pTagStartIndex, 1);
    }
  });
}

md.use(removeFirstPTag);

export default md;
