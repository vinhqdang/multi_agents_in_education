# Who designs the tutor? Human–AI collaboration, invisible work and sustainable HRM for academic staff in Asia–Pacific higher education

*Conceptual paper. Submission to the Asia Pacific Journal of Human Resources special issue "Human–AI Collaboration and Sustainable HRM in the Asia–Pacific".*

*Anonymised for double-blind review. Text in [square brackets] is still open for the author to confirm or fill in. Citation status is tracked in `references_status.md`; no reference is final until marked verified there.*

---

## Abstract

Universities across the Asia–Pacific are adopting generative AI agents that tutor students, generate practice tasks and return instant feedback. Research on these tools has focused on students. Much less is known about what happens to the academic staff who design, configure and oversee them. This paper argues that AI tutor agents do not simply automate teaching work; they move it. Feedback production shifts from the academic to the agent, while design, orchestration, verification and accountability work shifts to the academic, often without being recognised in workload models. Drawing on work design theory, the job demands–resources model and sustainable human resource management (HRM), and illustrated by the case of a lecturer who built multi-agent tutors for two undergraduate computing courses at a private international university in Vietnam, we develop a framework and six propositions. They explain when human–AI collaboration in teaching becomes a resource that sustains academics and when it becomes a hidden demand that depletes them, and how institutional HRM and Asia–Pacific contextual conditions (hierarchical governance, resource constraints and performance-driven private provision) shape that outcome. The paper contributes to HRM scholarship by extending the automation–augmentation debate to professional knowledge work in an under-studied sector and region, and offers practical guidance for HR and academic leaders on recognising and resourcing AI design work.

**Keywords:** human–AI collaboration; work design; job demands–resources; sustainable HRM; academic work; generative AI; Asia–Pacific; Vietnam

---

## 1. Introduction

Generative AI has entered universities faster than most institutions have been able to write policy for it. Alongside student use of general-purpose chatbots, a quieter change is under way: academics are building or configuring AI agents that act on their behalf with students. These agents generate exercises, answer questions, and give immediate feedback on submitted work, at a scale and speed no individual teacher can match. In computing education, where feedback on code is frequent, technical and time-consuming, the appeal is obvious.

Most research on these tools asks whether students learn more (e.g., Bastani et al., 2025; Yan et al., 2025). That question matters, but it leaves out the people who make the tools work. An AI tutor in a university course is not a finished product that arrives from outside. Someone has to decide what it should do, write and test its instructions, check that its outputs are correct, adjust it when it fails, explain it to students and answer for it when something goes wrong. In many institutions that someone is an individual academic acting on their own initiative.

This is an HRM question. How AI changes job design, task allocation, skill requirements and employee wellbeing is at the centre of current HRM debates (Budhwar et al., 2023; Parker & Grote, 2022), and the special issue to which this paper responds asks how AI-enabled work systems can be made sustainable in the Asia–Pacific. Academic staff are a large professional workforce whose work is already marked by intensification and blurred boundaries, and whose employers vary widely across the region in resources, governance and market position. Yet academics as employees rarely appear in HRM research on AI, and the education literature rarely treats AI adoption as a matter of work design.

We address this gap with a conceptual paper. Our central argument is that AI tutor agents do not automate teaching work so much as **relocate** it. The visible, countable part of the job (producing feedback for each student) moves to the agent. A less visible part (designing, orchestrating, verifying and being accountable for the agent's behaviour) moves to the academic. Whether this relocation sustains or depletes academic staff depends on whether institutions see and resource the new work, and on contextual conditions that are distinctive in parts of the Asia–Pacific.

We ask three questions:

1. How does the deployment of AI tutor agents reconfigure the tasks of academic staff?
2. Under what conditions do the resulting changes act as job resources rather than job demands?
3. How do sustainable HRM practices and Asia–Pacific contextual conditions shape these outcomes?

We build on three bodies of theory: work design theory, which treats job characteristics as consequences of organisational and technological choices (Parker & Grote, 2022; Hackman & Oldham, 1976); the job demands–resources (JD-R) model, which explains how job characteristics lead to strain or engagement (Bakker & Demerouti, 2007, 2017); and sustainable HRM, which asks whether HR systems regenerate or deplete the human resource base they rely on (Ehnert, 2009; Kramar, 2014). We illustrate the argument with a case from the first author's own practice: the design and deployment of multi-agent tutors in two undergraduate computing courses at a private international university in Vietnam.

The paper makes three contributions. First, it extends the automation–augmentation debate (Raisch & Krakowski, 2021) to professional knowledge work in higher education, showing that augmentation at the level of the service (students receive more feedback) can coincide with intensification at the level of the job. Second, it identifies *AI design and oversight work* as a category of largely invisible work (Star & Strauss, 1999) that HRM systems need to recognise. Third, it specifies Asia–Pacific contextual conditions under which this work is more likely to be individualised and unresourced, responding to calls for context-sensitive HRM research in the region (Budhwar et al., 2023; Cooke, 2018).

## 2. AI agents and the changing work of academics

### 2.1 From tools to agents

Earlier educational technologies, such as learning management systems or automated test runners, were tools that academics used. Current generative AI agents differ in two ways that matter for work design. First, they act with some autonomy: they decide, within limits set by their designer, what to say to a student, which exercise to give next and how to judge an answer. Second, their behaviour is set by natural-language instructions, examples and configuration choices rather than by conventional programming. This makes them accessible to non-specialists, but it also means their quality depends on design work that is iterative, judgement-heavy and hard to see from outside.

A single deployment may combine several agents with different roles, for example one that generates exercises, one that gives feedback on submissions, and one that runs an interactive coding task. Coordinating them adds a layer of work: the academic must decide how the agents divide labour, what each is allowed to do, and how their outputs fit the course's learning goals and assessment rules.

### 2.2 The augmentation promise and its limits

The dominant management framing presents AI as either automating tasks (replacing human effort) or augmenting them (extending human capability), with augmentation usually seen as the more desirable path (Raisch & Krakowski, 2021). In teaching, AI tutors are typically justified as augmentation: they give each student more practice and faster feedback than one academic can provide.

Raisch and Krakowski (2021) argue that automation and augmentation are interdependent over time: augmentation creates the knowledge that later enables automation, and automation creates new demands for human oversight. Applied to teaching, this suggests that when an academic delegates feedback production to an agent, the job does not shrink; it changes shape. The academic stops writing many individual comments and starts specifying, testing and supervising the system that writes them. Studies of professionals using AI in other fields point the same way: using AI for consequential judgements requires additional effort to interpret, check and take responsibility for its outputs (Lebovitz et al., 2022), and AI that takes over core tasks can unsettle professionals' sense of their role (Strich et al., 2021).

Evidence from students reinforces the importance of design. In a field experiment with high school mathematics students, unrestricted access to a general chatbot improved performance during practice but reduced performance on later tests, while a version with built-in pedagogical safeguards largely avoided that harm (Bastani et al., 2025). The distinction between performance during AI use and durable learning (Yan et al., 2025) means that whether an AI tutor helps students depends heavily on choices made by whoever designs it. In HRM terms, the quality of the service rests on design labour.

### 2.3 Academic work in the Asia–Pacific

Academic work across the region is shaped by rapid expansion of higher education, internationalisation, rising performance management and a large private and transnational sector [verified sources on Asia–Pacific and Vietnamese higher education to be added]. In many systems, teaching loads are high, contracts are often fixed-term in private institutions, and workload models count contact hours and student numbers more readily than development work. Generative AI is being introduced into this context with high expectations of efficiency and quality (Watermeyer et al., 2024), but with limited attention to who bears the cost of making it work.

## 3. Theoretical foundations

### 3.1 Work design

Work design theory holds that the content and organisation of tasks, activities and responsibilities shape motivation, wellbeing and performance (Hackman & Oldham, 1976; Morgeson & Humphrey, 2006). Parker and Grote (2022) argue that digital technologies make work design more important, not less, because the same technology can enrich or impoverish jobs depending on how it is implemented. Technology does not determine job characteristics; choices about its design and deployment do. The sociotechnical tradition makes the same point: technical and social systems must be designed together (Trist & Bamforth, 1951).

For academic staff using AI agents, the relevant characteristics include autonomy (who decides what the agent does), task variety and skill variety (new design and verification tasks), task significance (reaching more students), feedback from the job (usage data and student responses) and workload.

### 3.2 Job demands–resources

The JD-R model classifies job characteristics as demands, which require sustained effort and carry physiological and psychological costs, and resources, which help achieve goals, reduce demands or stimulate growth (Demerouti et al., 2001; Bakker & Demerouti, 2007). Demands drive a health-impairment process leading to strain and burnout; resources drive a motivational process leading to engagement. Resources also buffer the effect of demands, and employees can change their own demands and resources through job crafting (Bakker & Demerouti, 2017; Tims et al., 2012; Wrzesniewski & Dutton, 2001).

Technology-related demands have been studied as technostress: the strain that arises when technology increases work pace and volume, intrudes into personal time, or requires constant updating of skills (Tarafdar et al., 2007). Technology can also generate positive stress, or "techno-eustress", when it is experienced as a challenge (Tarafdar et al., 2019). This distinction matters for AI design work, which can be energising for some academics and exhausting for others.

### 3.3 Sustainable HRM

Sustainable HRM extends strategic HRM by asking whether HR practices reproduce the human resources an organisation depends on, rather than simply extracting performance from them (Ehnert, 2009; Kramar, 2014). It draws attention to long-term effects on employee health, skills and willingness to stay, and to the tensions between short-term efficiency and long-term viability. Applied to AI, it asks whether the gains from AI adoption are achieved by depleting staff, for example by relying on unpaid or unrecognised effort, or by building their capacity.

### 3.4 Invisible work

Star and Strauss (1999) describe work that is necessary but not seen, counted or rewarded because it falls outside formal job descriptions or because its success makes it disappear. Configuring and maintaining AI agents fits this description closely. When an agent works well, students see only its output; the effort that made it work is invisible. When it fails, the academic is visible as the person responsible.

## 4. An illustrative case

We use a case from the first author's own teaching to illustrate the framework. Following conventions for conceptual papers, the case is used to make the argument concrete, not to test it (Jaakkola, 2020; Whetten, 1989). We describe it as a reflexive account and note the author's dual role as designer and analyst in Section 7.

The setting is a private international university in Vietnam that offers undergraduate degrees in partnership with a foreign institution. In [semester and year], the lecturer responsible for two undergraduate computing courses, an introductory programming and algorithms course and an introduction to computing science, each with about 35 students, designed and deployed a set of AI tutor agents. The agents generated practice exercises, gave students instant feedback on their work and ran interactive coding tasks. They were built on a commercial large language model chosen in part because it was inexpensive to run. The institution's ethics process approved the use of the agents in teaching and the collection of related data.

The deployment was initiated by the lecturer rather than by the institution. [Confirm: whether the institution provided time allocation, funding for model access, technical support or training; who paid for model usage; whether the work counted in the workload model.] The lecturer designed the agents' roles, wrote and refined their instructions, tested their outputs against course content and monitored how students used them. [Confirm: approximate time spent on design and maintenance before and during the semester, and how this compared with the time previously spent on writing feedback by hand.]

Student activity on the course site increased markedly after the agents were introduced, from [figure] to [figure] [confirm the measure, e.g., share of students active each week]. This observation is relevant here not as evidence of learning but because it changed the lecturer's work: more student activity meant more agent output to monitor, more questions about the agents' responses and more visibility of the courses within the institution. [Confirm: any examples of agent errors the lecturer had to correct, student questions about agent feedback, or requests from colleagues or managers to extend the approach.]

Three features of the case inform the framework. First, the work of feedback did not disappear; it moved from writing comments to designing and checking the system that wrote them. Second, much of this work was invisible in formal terms [confirm]. Third, the decisions that most affected students' experience, such as what the agents should and should not do, were made by one academic, using individual judgement, under cost constraints.

## 5. A framework of human–AI collaboration in academic teaching work

Figure 1 summarises the framework. AI tutor agent deployment reconfigures academic tasks (P1). The reconfiguration creates both new demands (P2) and new resources (P3), whose balance depends on how the deployment is initiated and controlled. Sustainable HRM practices moderate the conversion of demands into strain (P4). Asia–Pacific contextual conditions shape both the HRM response and the distribution of demands (P5). Student-facing outcomes feed back into institutional decisions about scaling, which can intensify demands (P6).

*Figure 1 [to be drawn]: AI tutor deployment → task reconfiguration (P1) → job demands (P2) and job resources (P3) → strain or engagement and sustained capacity; moderators: sustainable HRM practices (P4) and Asia–Pacific context (P5); feedback loop from student-facing outcomes to institutional scaling (P6).*

### 5.1 Task reconfiguration

Deploying an AI tutor agent changes the composition of teaching work. Tasks that involve producing individual feedback and practice material are partly delegated to the agent. New tasks appear: specifying the agent's pedagogical role and limits; writing and revising instructions; testing outputs for accuracy and alignment with assessment; coordinating several agents; monitoring use; handling exceptions; and explaining the system to students and colleagues. These tasks require a mix of disciplinary, pedagogical and technical judgement and are rarely described in academic job specifications.

> **Proposition 1.** The deployment of AI tutor agents reallocates academic teaching work from the direct production of feedback and practice material towards design, orchestration, verification and accountability tasks, rather than reducing total teaching work.

### 5.2 New demands

The new tasks carry demands that existing workload models are poorly placed to capture. Design and testing are front-loaded and unpredictable; verification is continuous, because agent outputs can be wrong in ways that are hard to spot; and accountability is concentrated, because the academic is answerable for outputs they did not write. These demands resemble the techno-overload and techno-uncertainty components of technostress (Tarafdar et al., 2007). When the work is invisible (Star & Strauss, 1999), it is neither allocated time nor rewarded, which turns it into an additional demand on top of an unchanged formal load.

> **Proposition 2.** The design, verification and accountability work created by AI tutor agents constitutes a job demand that is positively related to strain among academic staff, and this relationship is stronger when the work is not recognised in formal workload allocation.

### 5.3 New resources

The same reconfiguration can also add resources. Academics who design agents gain autonomy over a new part of their practice, use a wider range of skills, see their effort reach more students and receive rapid information about how students engage. These are classic motivating job characteristics (Hackman & Oldham, 1976; Morgeson & Humphrey, 2006). Whether they operate as resources depends on control. When academics initiate and shape the deployment, it functions as job crafting (Tims et al., 2012; Wrzesniewski & Dutton, 2001) and the demands are more likely to be experienced as challenges (Tarafdar et al., 2019). When the agent is imposed, standardised or monitored from above, the same tasks are more likely to feel like algorithmic control over teaching (Kellogg et al., 2020).

> **Proposition 3.** AI tutor agent deployment increases job resources (autonomy, skill variety, task significance and feedback) for academic staff, and the positive relationship between deployment and work engagement is stronger when academics retain control over the agents' design and use.

### 5.4 Sustainable HRM as a moderator

Sustainable HRM practices can determine whether AI design work regenerates or depletes academic capacity. Relevant practices include counting design and oversight work in workload models; providing time and funding for development and model access; offering training and peer support; setting governance rules that clarify responsibility for agent outputs; and recognising the work in promotion and performance review. These practices act as organisational resources that buffer the demands identified in P2 (Bakker & Demerouti, 2017) and signal that the institution values long-term staff capacity over short-term efficiency (Ehnert, 2009; Kramar, 2014).

> **Proposition 4.** Sustainable HRM practices that make AI design and oversight work visible and resourced weaken the relationship between that work and strain, and strengthen its relationship with engagement and retention of academic staff.

### 5.5 Asia–Pacific contextual conditions

Three conditions common in parts of the Asia–Pacific, and present in the illustrative case, are likely to shape these processes. First, hierarchical governance and high power distance (Hofstede, 2001) can mean that bottom-up innovations by individual academics are tolerated but not formally adopted, leaving them dependent on personal effort. Second, resource constraints, especially in private and emerging-economy institutions, can push academics towards cheaper models and do-it-yourself solutions, shifting cost and risk onto individuals. Third, performance-driven private and transnational provision rewards visible student-facing outcomes, which can encourage institutions to showcase successful pilots without investing in the work behind them. These conditions do not apply uniformly across the region, which itself varies greatly (Cooke, 2018), but they identify where the risk of individualised, unresourced AI design work is likely to be highest.

> **Proposition 5.** The relationship between AI tutor agent deployment and unrecognised academic workload is stronger in institutions characterised by hierarchical governance, constrained resources and performance-driven provision, contexts that are common in parts of the Asia–Pacific.

### 5.6 The scaling loop

Successful pilots generate visible signals, such as higher student activity, that institutions can use to justify wider rollout. If scaling takes the form of an expectation that other academics adopt similar tools, or that the original designer support more courses, without the corresponding resources, a resource that was crafted voluntarily becomes a mandated demand. This is the point at which augmentation at the level of the service turns into intensification at the level of the job.

> **Proposition 6.** Visible student-facing gains from AI tutor agents increase institutional pressure to scale their use; when scaling is not accompanied by the HRM practices in Proposition 4, it converts AI design work from a crafted resource into an imposed demand.

## 6. Discussion

### 6.1 Theoretical implications

For HRM research on AI, the framework shows that the unit of analysis matters. At the level of the service, AI tutors augment teaching; at the level of the job, they can intensify it. Most debates on automation and augmentation (Raisch & Krakowski, 2021) focus on the former. Our framework brings the latter into view and links it to established theories of work design and job demands and resources.

For work design theory, we add AI design and oversight as a distinct cluster of tasks with its own demands and resources. This cluster is likely to grow as organisations configure agents rather than buy finished systems, and it is not specific to universities: similar work exists wherever professionals tailor AI agents to their clients.

For sustainable HRM, we identify invisibility as a mechanism through which AI adoption can deplete human resources. Sustainable HRM has emphasised long-term effects on health and skills (Ehnert, 2009; Kramar, 2014); our analysis suggests that whether new work is seen and counted is a precondition for any sustainable response.

For Asia–Pacific HRM, we specify conditions under which the burden of AI adoption is likely to fall on individuals, adding to calls for research that treats context as an explanatory variable rather than a backdrop (Cooke, 2018; Budhwar et al., 2023).

### 6.2 Practical implications

For HR and academic leaders, the framework suggests five actions. First, make AI design and oversight work visible by including it in workload models and annual planning. Second, provide resources at the point of initiative: time release, institutional licences for models, technical support and peer networks. Third, clarify accountability for agent outputs, so that academics are not personally exposed for errors in systems the institution benefits from. Fourth, recognise the work in performance review and promotion, including as teaching scholarship. Fifth, when scaling successful pilots, scale the resources along with the expectations.

### 6.3 Research agenda

The propositions can be tested in several ways. Time-use and diary studies could document how teaching tasks change after AI deployment (P1). Surveys of academic staff could test the relationships between AI design work, recognition, strain and engagement, using validated JD-R and technostress measures (P2–P4). Comparative case studies across institutions and countries in the region could examine contextual conditions (P5). Longitudinal studies following pilots into institutional rollout could test the scaling loop (P6). Multi-level designs linking staff experiences to student outcomes would connect this work to the education literature on AI tutors.

## 7. Limitations and positionality

This is a conceptual paper; the propositions are theoretical and require empirical testing. The illustrative case is a single deployment in one institution and is drawn from the first author's own practice. This gives detailed insight into design work that is usually hidden, but it also means the account is that of the designer, and other stakeholders, such as students, colleagues and managers, may see it differently. We have used the case only to illustrate the framework and do not draw empirical conclusions from it. The framework focuses on teaching work; AI agents also affect research and administrative work, which we do not address.

## 8. Conclusion

AI tutor agents are often presented as a way to give students more support without more staff time. This paper argues that the staff time does not disappear; it moves into design, verification and accountability work that institutions rarely see. Whether that work sustains or depletes academics depends on whether HRM systems recognise and resource it, and on contextual conditions that make individualised, unresourced innovation more likely in parts of the Asia–Pacific. Treating academic AI design work as work is a first step towards a sustainable human–AI collaboration in higher education.

---

## Declarations

**Ethics statement.** No new data were collected for this conceptual paper. The illustrative case draws on a teaching deployment approved through the institution's ethics process [reference to be provided after review, to preserve anonymity].

**Data availability statement.** Data sharing is not applicable to this article as no new data were created or analysed.

**Conflict of interest statement.** The author(s) declare no conflict of interest. [Confirm; and declare any working relationship with the guest editors where required by the journal's policy.]

**Funding statement.** [None / funding details.]

**Author contributions (CRediT).** [To be completed.]

**Use of generative AI.** [To be completed in line with the journal's and Wiley's policy on AI-assisted writing.]

---

## References

Only references marked as verified in `references_status.md` will be retained. The list will be finalised in APA 7 once verification is complete.
