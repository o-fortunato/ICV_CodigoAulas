# Markdown Cheatsheet

A compact reference for common Markdown formatting (GitHub Flavored Markdown / KaTeX supported).

## Headings
Use `#` to `######` for levels 1–6.

```md
# H1
## H2
### H3
```

## Emphasis
- **Bold:** `**bold text**`
- *Italic:* `*italic text*` or `_italic text_`
- ***Bold + Italic:*** `***bold italic***`
- ~~Strikethrough:~~ `~~strikethrough~~`

## Code
- Inline code: `` `inline-code()` ``
- Code block (fenced, optional language):

```markdown
```js
console.log("hello")
```
```

## Blockquote
Use `>` at the start of the line:

> This is a quote.

Nested: prefix more `>` characters.

## Lists
- Unordered: `- item`, `* item`, or `+ item`
- Ordered: `1. First`, `2. Second`
- Task list (GitHub): `- [ ] todo`, `- [x] done`
- Nested lists: indent by two spaces (or a tab).

## Links & Images
- Link: `[text](https://example.com)`
- Reference-style:

```md
[ref]: https://example.com
[link][ref]
```

- Image: `![alt text](image.jpg)` or with title: `![alt](img.png "title")`
- Automatic link: `<https://example.com>`

## Tables (GFM)

```md
| Header 1 | Header 2 |
|---------:|:--------:|
| right    | center   |
```

## Horizontal Rule
Use `---`, `***`, or `___` on its own line.

## Inline HTML
Inline HTML is allowed for advanced formatting (e.g., `<br>`).

## Escaping Characters
Escape Markdown characters with `\` before them: `\*`, `\_`, `\{`, `\}` etc.

## Footnotes (renderer-dependent)

```md
See note[^1]

[^1]: Footnote text.
```

## Math (KaTeX/LaTeX style)
- Inline: `$E=mc^2$`
- Block:

$$
\int_0^1 x\,dx = \tfrac{1}{2}
$$

## Syntax Highlighting Tip
Specify a language after the opening backticks for colored code blocks (e.g., ` ```python `).

## Best Practices
- Keep lines under ~80 characters for readability.
- Use blank lines between block elements.
- Prefer descriptive link text.

---

If you want this saved under a different filename or added to the existing `README.md`, tell me which file name to use.