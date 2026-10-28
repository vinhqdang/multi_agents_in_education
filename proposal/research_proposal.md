# Research Proposal (draft)

**Special issue:** AI Agents in Education: Multi-level Engagement for Student Learning
(Computers and Education: Artificial Intelligence)
**Proposal due:** 30 November 2026 | **Send to:** Dr. Weijiao Huang (wjhuang.academic@gmail.com)
**Limit:** 500-1000 words, following the editors' Research Proposal template.

Fields in [square brackets] are still open and need real information from the authors.

---

## Title (working)

Teacher-configured multi-agent systems for exercise generation and instant feedback: links between teacher practices and university students' learning outcomes

## 1. Background and aim

[2-3 sentences on the problem, e.g. limited timely feedback and practice opportunities in introductory programming courses.]

We study a multi-agent system used in two undergraduate courses at British University Vietnam (BUV): Algorithms and Programming Concepts, and Introduction to Computing Science. The agents generate exercises, give students instant feedback, and produce interactive coding tasks. The study connects two levels of the special issue: the **student level** (learning outcomes and interaction with the agents) and the **teacher level** (how instructors configure and use the agents). Student learning is the central outcome; teacher practices are examined as the mechanism that shapes it.

## 2. Research questions

- RQ1. How do students' learning outcomes (retention, [precise measure]) differ between [the agent-supported cohort and the comparison cohort / levels of agent use]?
- RQ2. Which teacher design and configuration decisions ([e.g. exercise difficulty settings, feedback style, oversight actions]) are associated with differences in student outcomes?
- RQ3. Do student-agent interaction patterns (from logs) mediate or moderate the link between teacher practices and learning outcomes?
- RQ4. Does the system improve learning (retention, transfer) or only immediate task performance? (Yan et al., 2025)

## 3. Agent description (TEP-AIED: transparency)

| Item | Description |
|---|---|
| Educational goal | Practice and instant feedback in introductory programming and computing concepts |
| Agents and roles | Tutor agents that generate exercises, give instant feedback and run interactive coding tasks [list each agent and its role] |
| Underlying model(s) | Gemini 3.8 Flash [confirm exact model ID, version/date, temperature, tools used] |
| Information used | [student submissions, past attempts, rubric, course materials, teacher settings] |
| Pedagogical actions | [exercise selection and difficulty, hints, corrective feedback, explanation] |
| Adaptation rule | [how the next exercise or feedback depends on the student's input] |
| Human oversight | [what teachers review, edit or override, and when] |

## 4. Theory and design principles

[Name the framework, e.g. self-regulated learning, feedback literacy, formative assessment, or self-determination theory. State which design decision each principle drove, and what the findings would mean for the theory.]

## 5. Design and participants

- Setting: BUV; Algorithms and Programming Concepts and Introduction to Computing Science; semester [ ]; ethics approval granted by BUV [reference ID, date]
- Students: n = 35 per course (N = 70 in total, [confirm no overlap]); instructors: [n; the lead author teaches both courses?]
- Design: [RCT / quasi-experiment / cohort comparison / longitudinal], duration [ ] weeks
- Condition/assignment: [ ]

## 6. Data sources and measures

- **Student learning outcomes:** [pre/post test, exam scores, delayed retention test, transfer task]; distinction between performance during the task and learning measured afterwards.
- **Process data:** system logs (number and timing of attempts, feedback requests, revision after feedback).
- **Teacher data:** [configuration records, reflection logs, classroom observations, interviews].
- **Self-reports (supplementary only):** [motivation, perceived feedback quality].

## 7. Analysis plan

[e.g. multilevel models with students nested in classes/teachers; mediation by interaction patterns; thematic analysis of teacher logs integrated with the quantitative results.] Multiple data sources are triangulated.

## 8. Current status and preliminary findings

Data collection: complete. Analysis: [status]. Preliminary finding to be verified before submission: retention rose from [10%] to [90%]. Before this goes into the proposal we must fix: (a) what "retention" means (re-enrolment/course completion, or delayed recall of content), (b) the comparison (previous cohort, same students over time, or control group), (c) the exact numerators and denominators, and (d) whether the change can be attributed to the agents rather than to other changes in the course.

## 9. Ethics and open science

Approved by BUV's research ethics process [reference ID]. [Consent procedure, anonymisation of logs, what student data is sent to the Gemini API.] Preregistration/data link: [OSF URL or planned date]. Materials shared: [prompts, agent configuration, anonymised data].

## 10. Contribution to the special issue

Empirical link between teacher practices and student learning with AI agents (levels 1 and 2); evidence on learning versus performance; explicit translation of [theory] into agent design.

## References (to confirm)

- Hwang, G. J., Xie, H., Wah, B. W., & Gasevic, D. (2026). Presenting your AI in education research with rigor: The TEP-AIED model. *Computers and Education: Artificial Intelligence*, 100598.
- Yan, L., Greiff, S., Lodge, J. M., & Gasevic, D. (2025). Distinguishing performance gains from learning when using generative AI. *Nature Reviews Psychology*, 4(7), 435-436.
