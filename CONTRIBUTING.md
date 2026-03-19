# Contributing to BEP Field Lab

Thanks for your interest in contributing! BEP Field Lab is a single-file browser-based research tool, so contributions tend to be focused and self-contained.

## Ways to Contribute

- **Bug reports** — open an issue describing the problem, your browser/OS, and steps to reproduce.
- **Feature requests** — open an issue with a clear description of the proposed feature and why it would be useful for BEP research or education.
- **Code contributions** — fork the repo, make your changes, and submit a pull request.
- **Theoretical feedback** — if you have suggestions for improving the BEP field dynamics model, Fourth Field module, or bifurcation analysis, open an issue or discussion.

## Guidelines

1. **Single-file architecture** — the app lives in one self-contained HTML file with no server-side dependencies. Please keep it that way.
2. **Browser-only** — all computation runs client-side. No external API calls, no login, no data leaves the user's browser.
3. **Keep it accessible** — the tool is designed for researchers, students, and curious people. Clear labels, readable code comments, and intuitive UI matter.
4. **Test before submitting** — open the file in at least two browsers (Chrome + Firefox recommended) and verify your changes don't break data upload, field computation, Fourth Field analysis, or export functionality.
5. **Respect the framework** — BEP Field Lab implements the Belonging–Energy–Prediction theoretical framework. Keep that framing in any documentation or UI text.

## Code Style

- Vanilla JS, no frameworks (the file must remain self-contained).
- Use `const` / `let`, never `var`.
- Descriptive variable names; comments for non-obvious logic.
- CSS custom properties (variables) for colors and theming.

## Pull Request Process

1. Fork and create a feature branch (`git checkout -b feature/my-feature`).
2. Make your changes in `index.html`.
3. Test thoroughly (data upload, field mapping, computation, Fourth Field, export).
4. Submit a PR with a clear description of what changed and why.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Contact

For questions, reach out to **Nicolas B. Quiroz, MD** via [GitHub](https://github.com/BEPframework).
