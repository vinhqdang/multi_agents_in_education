# Literature review notes (working draft, round 1)

Scope: LLM-based tutor agents that generate exercises and give instant feedback in introductory university programming and computing courses; how teacher design choices connect to student learning (not only engagement).

Form: narrative/integrative review. Every source carries a verification status. Nothing below should be cited in the manuscript until its status is "verified".

## 1. Candidate theoretical frame

**Self-regulated learning (SRL) combined with formative feedback.** The tutor agents are a feedback and practice environment; the teacher configures what feedback is given and when; the student learning outcome depends on whether feedback supports regulation (planning, monitoring, reflection) rather than replacing student effort. This frame lets the study ask a theory-level question: which agent design features (hinting versus answer-giving, exercise sequencing, human oversight) produce learning rather than performance.

Frame sources still to find and verify: Zimmerman's SRL model, Nicol and Macfarlane-Dick (2006) on feedback and self-regulation, and a cognitive-load source for worked examples in programming. Not yet searched.

## 2. Sources found

| # | Source | What it contributes | Status |
|---|---|---|---|
| 1 | Hattie & Timperley (2007). The power of feedback. *Review of Educational Research*, 77(1), 81-112. DOI 10.3102/003465430298487 | Feedback model (task, process, self-regulation, self levels); effects depend on type and timing | Bibliographic details and DOI confirmed across several record pages. Content summary above is standard; counts of studies not checked |
| 2 | Yan, Greiff, Lodge & Gasevic (2025). Distinguishing performance gains from learning when using generative AI. *Nature Reviews Psychology*, 4(7), 435-436. DOI 10.1038/s44159-025-00467-5 | Performance gains during AI use are not learning; the special issue's central distinction | Bibliographic details and DOI confirmed by search. Full text not read |
| 3 | Bastani et al. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS*, 122(26), e2422633122 | Field experiment (about 1,000 students, Turkey): unrestricted GPT raised practice performance but lowered later exam results; a guardrailed tutor largely removed the harm | Journal, volume and article number confirmed. DOI not directly seen; likely 10.1073/pnas.2422633122, verify. Effect sizes not checked against the paper |
| 4 | "When More Engagement Doesn't Mean More Learning: LLM Tutors and Self-Regulated Learning" (ICER 2026 programme entry) | Directly on point: preregistered study in CS1 (N = 1,059, three-arm crossover) on engagement versus learning with LLM tutors | Only the abstract and design were retrieved. Authors, DOI and results unverified. Highest priority to read in full |
| 5 | Evaluating the Effectiveness of LLMs in Introductory Computer Science Education: A Semester-Long Field Study (arXiv:2404.13414) | CodeTutor field study (about 50 students); experimental group improved final scores | arXiv record located; numbers come from a secondary summary. Check the primary paper and the published version |
| 6 | AI Meets the Classroom: When Do Large Language Models Harm Learning? (arXiv:2409.09047) | Large randomized trial in an online coding class (about 5,800 students): possible benefits, possible harms to engagement | Abstract-level only; authors and publication status unverified |
| 7 | Chu et al. (2025). LLM Agents for Education: Advances and Applications. *Findings of EMNLP* | Survey of LLM agents in education, including multi-agent designs and feedback generation | Located on ACL Anthology; details not checked |
| 8 | A January 2026 systematic review of 61 empirical studies of automated feedback in programming education | Most systems are fully automated and focus on error detection and correctness, with little on pedagogy or teacher roles | Title and authors not retrieved. Unverified |
| 9 | Survey of LLM-based applications in programming education: balancing automation and human oversight (arXiv:2510.03719) | Formative code feedback, assessment, knowledge modelling; human oversight | arXiv record located; unverified details |

Search note: the search tool returned several records with unusual arXiv identifiers and 2026 dates. Treat any identifier as provisional until opened on the publisher or arXiv page.

## 3. Emerging argument (draft, for discussion)

1. Instant feedback from LLM tutors reliably raises engagement and in-task performance; evidence on durable learning is mixed (sources 3, 4, 5, 6).
2. Where harm appears, it is linked to students using the tool as a crutch; guardrails in the tutor design reduce it (source 3). Guardrail design is a teacher and designer decision, which is the link between the student and teacher levels the special issue asks for.
3. Existing reviews of automated feedback in programming centre on technical correctness and rarely examine teacher design decisions or the learning-versus-performance distinction (sources 2, 8, 9).
4. Gap this study can fill: multi-agent tutors configured by the course instructor in two authentic courses, with the instructor's design decisions documented and related to student learning outcomes and interaction patterns.

## 4. Search plan for round 2

- Zimmerman (SRL), Nicol and Macfarlane-Dick (2006), Sweller or related cognitive load work, Kirschner et al. on guidance in instruction.
- Immediate versus delayed feedback in programming; hint-giving versus answer-giving in LLM tutors.
- Teacher-configured AI tutors: customisation, oversight, and effects on students (for the teacher level).
- Multi-agent LLM tutors in education with empirical learning outcomes.
- Open the full text of sources 4, 5, 6 and 8, and replace secondary summaries with figures taken from the papers.
