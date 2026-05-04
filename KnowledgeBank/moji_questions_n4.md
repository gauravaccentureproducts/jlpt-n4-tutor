# JLPT N4 Moji Questions

Source-of-truth question bank. Build pipeline parses into `data/questions.json`. Schema per §17 / Appendix A.6.

Question format:
```
### Q<N>
**Stem:** <prompt>
**Choices:**
1. <choice>
2. <choice>
3. <choice>
4. <choice>
**Answer:** <N>
**Explanation:** <english>
**Distractor explanations:**
- <wrong choice>: <why wrong, contrast with correct>
```


## Engine display note

For mock-test mode, the app's test engine MUST hide the `**Answer:**` line and rationale until the student commits an answer. The visible-by-default format here is for self-study reference; runtime test rendering is the engine's responsibility.

---

## Mondai 1
## Mondai 2
## Mondai 3
