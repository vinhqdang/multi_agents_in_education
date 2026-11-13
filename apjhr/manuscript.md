# Less work or more? AI tutor agents, invisible academic labour and the substitution trap in Asia–Pacific higher education

*Conceptual paper. Submission to the Asia Pacific Journal of Human Resources special issue "Human–AI Collaboration and Sustainable HRM in the Asia–Pacific".*

*Anonymised for double-blind review. Text in [square brackets] is still open for the author to confirm or fill in. Reference verification is recorded in `references_status.md`.*

---

## Abstract

Universities across the Asia–Pacific are adopting generative AI agents that tutor students, generate practice tasks and return instant feedback. These tools are often expected to reduce academic workload, and some institutions may see them as a reason to employ fewer teaching staff. This paper asks whether AI tutor agents actually lighten the work of academics, and what happens when institutions act on the assumption that they do. We argue that the agents do not remove teaching work but relocate it. Feedback production shifts from the academic to the agent, while design, orchestration, verification and accountability work shifts to the academic, usually without being recognised in workload models. Because the work that disappears is visible and the work that appears is not, institutions can misread AI adoption as freed capacity and cut or casualise teaching positions, removing the people whose hidden work keeps the agents useful and raising job insecurity among those who remain. Drawing on work design theory, the job demands–resources model and sustainable human resource management (HRM), and illustrated by the case of a lecturer who built multi-agent tutors for two undergraduate computing courses at a private international university in Vietnam, we develop a framework and seven propositions. They explain when human–AI collaboration in teaching sustains academics and when it depletes them, how Asia–Pacific conditions (hierarchical governance, resource constraints and performance-driven private provision) increase the risk of a "substitution trap", and what HRM can do to avoid it. The paper extends the automation–augmentation debate to professional knowledge work in an under-studied sector and region and offers guidance for HR and academic leaders on recognising AI design work before making staffing decisions.

**Keywords:** human–AI collaboration; work design; job insecurity; job demands–resources; sustainable HRM; academic work; generative AI; Asia–Pacific; Vietnam

---

## 1. Introduction

Generative AI has entered universities faster than most institutions have been able to write policy for it. Alongside student use of general-purpose chatbots, a quieter change is under way: academics are building or configuring AI agents that act on their behalf with students. These agents generate exercises, answer questions, and give immediate feedback on submitted work, at a scale and speed no individual teacher can match. In computing education, where feedback on code is frequent, technical and time-consuming, the appeal is obvious.

Most research on these tools asks whether students learn more (e.g., Bastani et al., 2025; Yan et al., 2025). That question matters, but it leaves out the people who make the tools work. An AI tutor in a university course is not a finished product that arrives from outside. Someone has to decide what it should do, write and test its instructions, check that its outputs are correct, adjust it when it fails, explain it to students and answer for it when something goes wrong. In many institutions that someone is an individual academic acting on their own initiative.

This is an HRM question. How AI changes job design, task allocation, skill requirements and employee wellbeing is at the centre of current HRM debates (Bankins et al., 2024; Budhwar et al., 2023; Parker & Grote, 2022), and the special issue to which this paper responds asks how AI-enabled work systems can be made sustainable in the Asia–Pacific. Academic staff are a large professional workforce whose work is already marked by intensification and blurred boundaries, and whose employers vary widely across the region in resources, governance and market position. Yet academics as employees rarely appear in HRM research on AI, and the education literature rarely treats AI adoption as a matter of work design.

The question is also pressing for a second reason. AI tools are widely expected to reduce the labour needed for routine knowledge work (Frey & Osborne, 2017), and universities under financial pressure have an incentive to take that expectation at face value. If an AI tutor answers students' questions and marks their practice exercises, it is tempting to conclude that fewer teaching staff, larger classes or fewer tutors are needed. For academics, this turns a teaching innovation into a possible threat to their own jobs.

We address both issues with a conceptual paper. Our central argument is that AI tutor agents do not automate teaching work so much as **relocate** it. The visible, countable part of the job (producing feedback for each student) moves to the agent. A less visible part (designing, orchestrating, verifying and being accountable for the agent's behaviour) moves to the academic. Because what disappears is easy to see and what appears is not, institutions can misread AI adoption as freed capacity. Acting on that misreading, by cutting or casualising teaching positions, removes the people whose hidden work keeps the agents useful and raises job insecurity among those who remain. We call this the **substitution trap**.

We ask four questions:

1. Does the deployment of AI tutor agents reduce the work of academic staff, or reconfigure it?
2. Under what conditions do the resulting changes act as job resources rather than job demands?
3. How do sustainable HRM practices and Asia–Pacific contextual conditions shape these outcomes?
4. What happens when institutions treat AI tutor agents as a substitute for teaching staff?

We build on three bodies of theory: work design theory, which treats job characteristics as consequences of organisational and technological choices (Parker & Grote, 2022; Hackman & Oldham, 1976); the job demands–resources (JD-R) model, which explains how job characteristics lead to strain or engagement (Bakker & Demerouti, 2007, 2017); and sustainable HRM, which asks whether HR systems regenerate or deplete the human resource base they rely on (Ehnert, 2009; Kramar, 2014). We illustrate the argument with a case from the first author's own practice: the design and deployment of multi-agent tutors in two undergraduate computing courses at a private international university in Vietnam.

The paper makes four contributions. First, it extends the automation–augmentation debate (Raisch & Krakowski, 2021) to professional knowledge work in higher education, showing that augmentation at the level of the service (students receive more feedback) can coincide with intensification at the level of the job. Second, it identifies *AI design and oversight work* as a category of largely invisible work (Star & Strauss, 1999) that HRM systems need to recognise. Third, it specifies Asia–Pacific contextual conditions under which this work is more likely to be individualised and unresourced, responding to calls for context-sensitive HRM research in the region (Budhwar et al., 2023; Cooke, 2018). Fourth, it explains how staffing decisions based on the visible effects of AI can undermine both the sustainability of academic work and the quality of the AI-supported service itself.

## 2. AI agents and the changing work of academics

### 2.1 From tools to agents

Earlier educational technologies, such as learning management systems or automated test runners, were tools that academics used. Current generative AI agents differ in two ways that matter for work design. First, they act with some autonomy: they decide, within limits set by their designer, what to say to a student, which exercise to give next and how to judge an answer. Second, their behaviour is set by natural-language instructions, examples and configuration choices rather than by conventional programming. This makes them accessible to non-specialists, but it also means their quality depends on design work that is iterative, judgement-heavy and hard to see from outside.

A single deployment may combine several agents with different roles, for example one that generates exercises, one that gives feedback on submissions, and one that runs an interactive coding task. Coordinating them adds a layer of work: the academic must decide how the agents divide labour, what each is allowed to do, and how their outputs fit the course's learning goals and assessment rules.

Three properties of these agents matter for the argument that follows. The first is **configurability**: their behaviour is not fixed by a vendor but shaped by whoever writes their instructions, which places design responsibility close to the individual teacher. The second is **fallibility**: generative models produce fluent output that can be wrong, so their use requires continuing verification rather than a one-off check. The third is **scale**: once deployed, an agent can interact with every student in a course at any hour, so both its benefits and its errors multiply. Configurability creates design work, fallibility creates verification work, and scale magnifies the consequences of both. None of these properties is captured by the common image of AI as a tool that simply saves time.

### 2.2 The augmentation promise and its limits

The dominant management framing presents AI as either automating tasks (replacing human effort) or augmenting them (extending human capability), with augmentation usually seen as the more desirable path (Raisch & Krakowski, 2021). Field evidence from other settings supports the augmentation case: in a large customer-support operation, access to a generative AI assistant raised productivity, with the largest gains for less experienced workers (Brynjolfsson et al., 2025). In teaching, AI tutors are typically justified in similar terms: they give each student more practice and faster feedback than one academic can provide.

Raisch and Krakowski (2021) argue that automation and augmentation are interdependent over time: augmentation creates the knowledge that later enables automation, and automation creates new demands for human oversight. Applied to teaching, this suggests that when an academic delegates feedback production to an agent, the job does not shrink; it changes shape. The academic stops writing many individual comments and starts specifying, testing and supervising the system that writes them. Studies of professionals using AI in other fields point the same way: using AI for consequential judgements requires additional effort to interpret, check and take responsibility for its outputs (Lebovitz et al., 2022), and AI that takes over core tasks can unsettle professionals' sense of their role (Strich et al., 2021).

Evidence from students reinforces the importance of design. In a field experiment with high school mathematics students, unrestricted access to a general chatbot improved performance during practice but reduced performance on later tests, while a version with built-in pedagogical safeguards largely avoided that harm (Bastani et al., 2025). The distinction between performance during AI use and durable learning (Yan et al., 2025) means that whether an AI tutor helps students depends heavily on choices made by whoever designs it. In HRM terms, the quality of the service rests on design labour.

### 2.3 Academic work in the Asia–Pacific

HRM practices and their outcomes differ substantially across the Asia–Pacific, reflecting institutional, cultural and economic conditions (Budhwar et al., 2016; De Cieri et al., 2022). Academic work in the region is no exception. Studies of university academics in Australia and New Zealand report high levels of occupational stress linked to workload and job insecurity (Lee et al., 2022). In Vietnam, where higher education has expanded and internationalised rapidly, research on public universities has pointed to limited HRM capacity to support academic work beyond teaching (Nguyen, 2016). Private and transnational institutions add further pressures, since their market position depends on visible indicators of teaching quality and student experience [the author may add a verified source on Vietnamese private or transnational higher education here]. Across these settings, workload models tend to count contact hours and student numbers more readily than development work. Generative AI is being introduced into this context with high expectations of efficiency and quality (Watermeyer et al., 2024), but with limited attention to who bears the cost of making it work. University teachers differ widely in how they use AI and in their confidence with it, and many report unmet needs for professional development (Mah & Groß, 2024).

### 2.4 AI in HRM research

HRM research on AI has concentrated mainly on AI used by organisations to manage people: in recruitment and selection, workforce analytics and algorithmic management (Meijerink et al., 2021; Prikshat et al., 2023; Vrontis et al., 2022). Reviews have mapped its antecedents, uses and consequences for HR functions (Malik et al., 2023) and for international HRM (Budhwar et al., 2022), and qualitative work in the region has examined how HR professionals experience AI adoption (Sithambaram & Tajudeen, 2023). The arrival of generative AI has turned attention to employees who work alongside AI in their own tasks (Budhwar et al., 2023; Chowdhury et al., 2024). A multilevel review of AI in organisations calls for research on how AI changes the content of jobs and employees' experience of work (Bankins et al., 2024).

Two features of the present case are less well covered. First, the AI is not introduced by HR or management but built by an employee for use with the organisation's clients, here students. Second, the employee is a professional whose work is only partly codified, so the effort required to make AI useful is easily overlooked. Both features are increasingly common as configurable agents spread, and both have direct implications for how HR systems define, allocate and reward work.

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

### 3.5 Integrating the lenses

Each lens on its own explains part of the problem. Work design theory explains why the same AI deployment can enrich or impoverish a job, but it says less about how the resulting job characteristics translate into wellbeing over time. The JD-R model supplies that mechanism, but it treats demands and resources as given rather than asking how they come to be defined and counted. The concept of invisible work fills this gap: whether a task is formally recognised determines whether it is allocated time, and therefore whether it adds to or replaces existing demands. Sustainable HRM, finally, places these processes within the organisation's choices about how to use and reproduce its human resources, including choices about staffing.

Combined, the lenses give a sequence that structures the framework in Section 5. Technology deployment changes the task composition of the job (work design). Some of the new tasks are recognised and some are not (invisible work). Unrecognised tasks act as additional demands, while recognised and self-directed ones can act as resources (JD-R). Institutional HRM practices determine which outcome dominates and whether visible efficiency gains are converted into staffing cuts (sustainable HRM). Contextual conditions in the Asia–Pacific shape each step.

This integration also clarifies what the framework does not claim. It does not claim that AI tutor agents are harmful to academics, nor that they are beneficial. It claims that their effect on academic work is indeterminate at the level of technology and determined by organisational choices that HRM can influence. This is consistent with the work design view that technology's effects on jobs are a matter of design rather than destiny (Parker & Grote, 2022).

## 4. An illustrative case

We use a case from the first author's own teaching to illustrate the framework. Following conventions for conceptual papers, the case is used to make the argument concrete, not to test it (Jaakkola, 2020; Whetten, 1989). We describe it as a reflexive account and note the author's dual role as designer and analyst in Section 7.

The setting is a private international university in Vietnam that offers undergraduate degrees in partnership with a foreign institution. In [semester and year], the lecturer responsible for two undergraduate computing courses, an introductory programming and algorithms course and an introduction to computing science, each with about 35 students, designed and deployed a set of AI tutor agents. The agents generated practice exercises, gave students instant feedback on their work and ran interactive coding tasks. They were built on a commercial large language model chosen in part because it was inexpensive to run. The institution's ethics process approved the use of the agents in teaching and the collection of related data.

The deployment was initiated by the lecturer rather than by the institution. [Confirm: whether the institution provided time allocation, funding for model access, technical support or training; who paid for model usage; whether the work counted in the workload model.] The lecturer designed the agents' roles, wrote and refined their instructions, tested their outputs against course content and monitored how students used them. [Confirm: approximate time spent on design and maintenance before and during the semester, and how this compared with the time previously spent on writing feedback by hand.]

Student activity on the course site increased markedly after the agents were introduced, from [figure] to [figure] [confirm the measure, e.g., share of students active each week]. This observation is relevant here not as evidence of learning but because it changed the lecturer's work: more student activity meant more agent output to monitor, more questions about the agents' responses and more visibility of the courses within the institution. [Confirm: any examples of agent errors the lecturer had to correct, student questions about agent feedback, or requests from colleagues or managers to extend the approach.]

Three features of the case inform the framework. First, the work of feedback did not disappear; it moved from writing comments to designing and checking the system that wrote them. Second, much of this work was invisible in formal terms [confirm]. Third, the decisions that most affected students' experience, such as what the agents should and should not do, were made by one academic, using individual judgement, under cost constraints.

## 5. A framework of human–AI collaboration in academic teaching work

Figure 1 summarises the framework. AI tutor agent deployment reconfigures academic tasks (P1). The reconfiguration creates both new demands (P2) and new resources (P3), whose balance depends on how the deployment is initiated and controlled. Sustainable HRM practices moderate the conversion of demands into strain (P4). Asia–Pacific contextual conditions shape both the HRM response and the distribution of demands (P5). Student-facing outcomes feed back into institutional decisions about scaling, which can intensify demands (P6), and into staffing decisions that treat the agents as a substitute for staff (P7).

*Figure 1 [to be drawn]: AI tutor deployment → task reconfiguration (P1) → job demands (P2) and job resources (P3) → strain or engagement and sustained capacity; moderators: sustainable HRM practices (P4) and Asia–Pacific context (P5); feedback loops from student-facing outcomes to institutional scaling (P6) and to substitution-based staffing decisions (P7).*

### 5.1 Task reconfiguration

Deploying an AI tutor agent changes the composition of teaching work. Tasks that involve producing individual feedback and practice material are partly delegated to the agent. New tasks appear: specifying the agent's pedagogical role and limits; writing and revising instructions; testing outputs for accuracy and alignment with assessment; coordinating several agents; monitoring use; handling exceptions; and explaining the system to students and colleagues. These tasks require a mix of disciplinary, pedagogical and technical judgement and are rarely described in academic job specifications.

Table 1 sets out the reconfiguration. The left column lists tasks that are partly delegated to the agents; the right column lists tasks that are created or expanded. The two columns are not equivalent in visibility. Tasks on the left are easy to count: numbers of comments written, exercises set, queries answered. Tasks on the right are harder to count because they are iterative, irregular and often done outside timetabled hours.

*Table 1. Reconfiguration of teaching tasks under AI tutor agent deployment*

| Tasks partly delegated to the agents (visible, countable) | Tasks created or expanded for the academic (less visible) |
|---|---|
| Writing individual feedback on practice work | Specifying each agent's pedagogical role, limits and tone |
| Producing practice exercises and variations | Writing, testing and revising agent instructions |
| Answering routine student questions | Checking agent outputs for accuracy and alignment with assessment |
| Running supervised practice sessions | Coordinating several agents and their division of labour |
| | Monitoring use and identifying failures or misuse |
| | Handling exceptions, complaints and disputed feedback |
| | Explaining the system to students, colleagues and managers |
| | Managing cost, data protection and model changes |
| | Bearing accountability for outputs the academic did not write |

Two qualifications apply. First, the balance between the columns is not fixed. Design work is front-loaded and may decline once the agents are stable, while verification and accountability are continuing. Over a longer period the net effect on workload may therefore fall, but only if the course and model remain stable, which is rarely the case when models are updated by their providers. Second, the right-hand tasks differ in kind, not only in amount: they are more judgement-intensive and carry more personal risk than the tasks they replace.

> **Proposition 1.** The deployment of AI tutor agents reallocates academic teaching work from the direct production of feedback and practice material towards design, orchestration, verification and accountability tasks, rather than reducing total teaching work.

### 5.2 New demands

The new tasks carry demands that existing workload models are poorly placed to capture. Design and testing are front-loaded and unpredictable; verification is continuous, because agent outputs can be wrong in ways that are hard to spot; and accountability is concentrated, because the academic is answerable for outputs they did not write. These demands resemble the techno-overload and techno-uncertainty components of technostress (Tarafdar et al., 2007). When the work is invisible (Star & Strauss, 1999), it is neither allocated time nor rewarded, which turns it into an additional demand on top of an unchanged formal load.

> **Proposition 2.** The design, verification and accountability work created by AI tutor agents constitutes a job demand that is positively related to strain among academic staff, and this relationship is stronger when the work is not recognised in formal workload allocation.

### 5.3 New resources

The same reconfiguration can also add resources. Academics who design agents gain autonomy over a new part of their practice, use a wider range of skills, see their effort reach more students and receive rapid information about how students engage. These are classic motivating job characteristics (Hackman & Oldham, 1976; Morgeson & Humphrey, 2006). Whether they operate as resources depends on control. When academics initiate and shape the deployment, it functions as job crafting (Tims et al., 2012; Wrzesniewski & Dutton, 2001) and the demands are more likely to be experienced as challenges (Tarafdar et al., 2019). When the agent is imposed, standardised or monitored from above, the same tasks are more likely to feel like algorithmic control over teaching (Kellogg et al., 2020).

The case illustrates why control matters. Because the lecturer initiated the deployment, decisions about what the agents should do, how far they should go in giving answers, and how to balance cost against quality were the lecturer's to make. These choices are a source of autonomy and professional meaning. The same choices, if made by a central unit and handed to academics as a standard tool, would leave academics with the verification and accountability tasks in Table 1 but without the design tasks that make them meaningful. The demands would remain while the resources would be removed. This asymmetry is the core of Proposition 3, and it connects to the concern that AI which takes over core professional judgements can weaken professional role identity (Strich et al., 2021).

> **Proposition 3.** AI tutor agent deployment increases job resources (autonomy, skill variety, task significance and feedback) for academic staff, and the positive relationship between deployment and work engagement is stronger when academics retain control over the agents' design and use.

### 5.4 Sustainable HRM as a moderator

Sustainable HRM practices can determine whether AI design work regenerates or depletes academic capacity. Relevant practices include counting design and oversight work in workload models; providing time and funding for development and model access; offering training and peer support, which many university teachers say they lack (Mah & Groß, 2024); setting governance rules that clarify responsibility for agent outputs; and recognising the work in promotion and performance review. These practices act as organisational resources that buffer the demands identified in P2 (Bakker & Demerouti, 2017) and signal that the institution values long-term staff capacity over short-term efficiency (Ehnert, 2009; Kramar, 2014).

Sustainable HRM is not free of tension here. Formalising AI design work in workload models makes it visible, but it can also make it auditable and standardised, which may reduce the autonomy that made it a resource in the first place. The sustainable HRM literature frames such tensions as paradoxes to be managed rather than resolved (Ehnert, 2009). In practice this suggests recognising the time and responsibility involved in AI design work without prescribing how it is done, and leaving pedagogical decisions about the agents with the academics who answer for them.

> **Proposition 4.** Sustainable HRM practices that make AI design and oversight work visible and resourced weaken the relationship between that work and strain, and strengthen its relationship with engagement and retention of academic staff.

### 5.5 Asia–Pacific contextual conditions

Three conditions common in parts of the Asia–Pacific, and present in the illustrative case, are likely to shape these processes. First, hierarchical governance and high power distance (Hofstede, 2001) can mean that bottom-up innovations by individual academics are tolerated but not formally adopted, leaving them dependent on personal effort. Second, resource constraints, especially in private and emerging-economy institutions, can push academics towards cheaper models and do-it-yourself solutions, shifting cost and risk onto individuals. Third, performance-driven private and transnational provision rewards visible student-facing outcomes, which can encourage institutions to showcase successful pilots without investing in the work behind them. Each condition affects a different step of the framework. Hierarchical governance affects recognition (P2 and P4): innovations that start from below are less likely to be written into workload models or policies. Resource constraints affect the balance of demands and resources (P2 and P3): when academics pay for or work around the limits of cheap models, verification and maintenance demands rise. Performance-driven provision affects the feedback loops (P6 and P7): visible gains in student activity are valuable in a competitive market, which increases both the pressure to scale and the temptation to translate efficiency into lower staffing costs. Labour market conditions add a further layer. Where a substantial share of teaching is done by staff on fixed-term or sessional contracts, as is common in private and transnational provision, the risks described in Proposition 7 fall on those with the least protection.

These conditions do not apply uniformly across the region, which itself varies greatly (Budhwar et al., 2016; Cooke, 2018; De Cieri et al., 2022), but they identify where the risk of individualised, unresourced AI design work is likely to be highest.

> **Proposition 5.** The relationship between AI tutor agent deployment and unrecognised academic workload is stronger in institutions characterised by hierarchical governance, constrained resources and performance-driven provision, contexts that are common in parts of the Asia–Pacific.

### 5.6 The scaling loop

Successful pilots generate visible signals, such as higher student activity, that institutions can use to justify wider rollout. If scaling takes the form of an expectation that other academics adopt similar tools, or that the original designer support more courses, without the corresponding resources, a resource that was crafted voluntarily becomes a mandated demand. This is the point at which augmentation at the level of the service turns into intensification at the level of the job.

> **Proposition 6.** Visible student-facing gains from AI tutor agents increase institutional pressure to scale their use; when scaling is not accompanied by the HRM practices in Proposition 4, it converts AI design work from a crafted resource into an imposed demand.

### 5.7 The substitution trap

The final step concerns staffing. Institutions observe the visible part of the change: students receive feedback without an academic writing it, and fewer student queries reach staff. They do not observe the design, verification and accountability work that P1 and P2 describe. From the institution's point of view, AI adoption therefore looks like freed capacity. Under financial pressure, this invites substitution: larger classes per academic, fewer sessional tutors or teaching assistants, non-renewal of fixed-term contracts, or the expectation that one designer now supports many courses.

Substitution based on this misreading has three consequences. First, it intensifies the work of those who remain, because the hidden work does not shrink when staff numbers do; it grows with the number of students and courses the agents serve. Second, it tends to fall first on the most precarious staff, such as sessional tutors and staff on fixed-term contracts, whose work is most easily described as routine feedback. Third, it raises job insecurity among academics more broadly. Job insecurity is associated with lower wellbeing and with withdrawal of discretionary effort (Shoss, 2017). In this setting, it creates a perverse incentive: academics who can build effective AI tutors may hesitate to do so, or to share what they have built, if visible success is likely to be used to justify cutting teaching positions. The institution then loses the bottom-up innovation it benefited from in the first place.

Substitution also carries a quality risk. The agents' value for students depends on design choices and continued oversight (Bastani et al., 2025; Yan et al., 2025). If the people who make those choices are removed or overloaded, the service the institution relied on to justify the cuts is likely to deteriorate.

> **Proposition 7.** When institutions interpret AI tutor agents as a substitute for teaching staff and reduce or casualise teaching positions on that basis, (a) the workload and strain of remaining academic staff increase, (b) job insecurity increases, especially among precarious staff, and (c) academics' willingness to develop and share AI innovations decreases. These effects are weaker when staffing decisions are preceded by an assessment of the design and oversight work the agents require.

## 6. Discussion

### 6.1 Theoretical implications

For HRM research on AI, the framework shows that the unit of analysis matters. At the level of the service, AI tutors augment teaching; at the level of the job, they can intensify it. Most debates on automation and augmentation (Raisch & Krakowski, 2021) focus on the former. Our framework brings the latter into view and links it to established theories of work design and job demands and resources.

For work design theory, we add AI design and oversight as a distinct cluster of tasks with its own demands and resources. This cluster is likely to grow as organisations configure agents rather than buy finished systems, and it is not specific to universities: similar work exists wherever professionals tailor AI agents to their clients.

For sustainable HRM, we identify invisibility as a mechanism through which AI adoption can deplete human resources. Sustainable HRM has emphasised long-term effects on health and skills (Ehnert, 2009; Kramar, 2014); our analysis suggests that whether new work is seen and counted is a precondition for any sustainable response.

For research on AI and employment, the substitution trap qualifies task-based predictions of labour displacement (Frey & Osborne, 2017). In professional work, the tasks AI performs are not simply removed from human jobs; they are partly replaced by new tasks of design and oversight that are harder to see. Staffing decisions that count only the removed tasks are likely to overestimate the labour saved.

For Asia–Pacific HRM, we specify conditions under which the burden of AI adoption is likely to fall on individuals, adding to calls for research that treats context as an explanatory variable rather than a backdrop (Bartram & Cooke, 2022; Budhwar et al., 2023; Cooke, 2018).

### 6.2 Boundary conditions and alternative views

Several boundary conditions limit the framework. It applies most directly to agents that academics configure themselves. Where an institution buys a finished system with little scope for local design, design work shrinks but verification and accountability remain, and the autonomy-related resources in Proposition 3 are likely to be weaker. It also applies most directly to courses where feedback is frequent and technical, as in computing; in disciplines where feedback is less frequent or more interpretive, the balance of delegated and new tasks may differ.

An alternative view holds that the additional work is a transitional cost: once academics learn to design agents and the tools mature, the hidden work will shrink and real savings will appear. The framework does not rule this out. It does suggest two reasons for caution. First, the models on which agents run change frequently and outside the institution's control, so stabilisation may be partial. Second, even if savings appear later, staffing decisions taken earlier on the basis of expected savings would already have produced the effects described in Proposition 7. The sequence of decisions matters as much as the eventual balance of work.

A second alternative view is that academics who build AI agents do so voluntarily and enjoy it, so their extra work is not an HRM problem. Voluntary effort is indeed central to Proposition 3. But sustainable HRM is concerned precisely with whether organisations rely on effort they do not recognise or reproduce (Kramar, 2014). Voluntary innovation that becomes an institutional expectation, or the basis for staffing decisions, is no longer purely voluntary.

### 6.3 Practical implications

For HR and academic leaders, the framework suggests six actions. First, make AI design and oversight work visible by including it in workload models and annual planning. Second, provide resources at the point of initiative: time release, institutional licences for models, technical support and peer networks. Third, clarify accountability for agent outputs, so that academics are not personally exposed for errors in systems the institution benefits from. Fourth, recognise the work in performance review and promotion, including as teaching scholarship. Fifth, when scaling successful pilots, scale the resources along with the expectations. Sixth, do not treat AI tutor adoption as evidence that teaching staff can be reduced. Before any change to staffing, class sizes or tutor allocations, assess the design, verification and accountability work the agents require, consult the staff who do it, and give particular attention to sessional and fixed-term staff. Making clear that successful AI innovation will not be used against those who produce it is also a condition for continued innovation.

### 6.4 Research agenda

The propositions can be tested in several ways. Time-use and diary studies could document how teaching tasks change after AI deployment (P1). Surveys of academic staff could test the relationships between AI design work, recognition, strain and engagement, using validated JD-R and technostress measures (P2–P4). Comparative case studies across institutions and countries in the region could examine contextual conditions (P5). Longitudinal studies following pilots into institutional rollout could test the scaling loop (P6). Institutional case studies and staffing data, combined with staff surveys on job insecurity and innovation behaviour, could test the substitution trap (P7), ideally comparing institutions that did and did not adjust staffing after AI adoption. Multi-level designs linking staff experiences to student outcomes would connect this work to the education literature on AI tutors.

## 7. Limitations and positionality

This is a conceptual paper; the propositions are theoretical and require empirical testing. The illustrative case is a single deployment in one institution and is drawn from the first author's own practice. This gives detailed insight into design work that is usually hidden, but it also means the account is that of the designer, and other stakeholders, such as students, colleagues and managers, may see it differently. We have used the case only to illustrate the framework and do not draw empirical conclusions from it. The framework focuses on teaching work; AI agents also affect research and administrative work, which we do not address.

## 8. Conclusion

AI tutor agents are often presented as a way to give students more support without more staff time. Our answer to the question in the title is that they do not, by themselves, mean less work for academics: the staff time does not disappear but moves into design, verification and accountability work that institutions rarely see. The danger is that institutions treat the visible savings as real and the hidden work as non-existent, and cut teaching positions accordingly. That would increase the burden on those who remain, fall hardest on precarious staff, discourage the innovation that made the tools useful, and ultimately weaken the service it was meant to protect. Whether that work sustains or depletes academics depends on whether HRM systems recognise and resource it, and on contextual conditions that make individualised, unresourced innovation more likely in parts of the Asia–Pacific. Treating academic AI design work as work is a first step towards a sustainable human–AI collaboration in higher education.

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

Bakker, A. B., & Demerouti, E. (2007). The Job Demands-Resources model: State of the art. *Journal of Managerial Psychology, 22*(3), 309–328. https://doi.org/10.1108/02683940710733115

Bakker, A. B., & Demerouti, E. (2017). Job demands–resources theory: Taking stock and looking forward. *Journal of Occupational Health Psychology, 22*(3), 273–285. https://doi.org/10.1037/ocp0000056

Bankins, S., Ocampo, A. C., Marrone, M., Restubog, S. L. D., & Woo, S. E. (2024). A multilevel review of artificial intelligence in organizations: Implications for organizational behavior research and practice. *Journal of Organizational Behavior, 45*(2), 159–182. https://doi.org/10.1002/job.2735

Bartram, T., & Cooke, F. L. (2022). Celebrating the 60th anniversary of the *Asia Pacific Journal of Human Resources*: What has been achieved and what more can be done. *Asia Pacific Journal of Human Resources, 60*(1), 3–21. https://doi.org/10.1111/1744-7941.12320

Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences, 122*(26), Article e2422633122. https://doi.org/10.1073/pnas.2422633122

Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at work. *The Quarterly Journal of Economics, 140*(2), 889–942. https://doi.org/10.1093/qje/qjae044

Budhwar, P., Chowdhury, S., Wood, G., Aguinis, H., Bamber, G. J., Beltran, J. R., Boselie, P., Lee Cooke, F., Decker, S., DeNisi, A., Dey, P. K., Guest, D., Knoblich, A. J., Malik, A., Paauwe, J., Papagiannidis, S., Patel, C., Pereira, V., Ren, S., . . . Varma, A. (2023). Human resource management in the age of generative artificial intelligence: Perspectives and research directions on ChatGPT. *Human Resource Management Journal, 33*(3), 606–659. https://doi.org/10.1111/1748-8583.12524

Budhwar, P., Malik, A., De Silva, M. T. T., & Thevisuthan, P. (2022). Artificial intelligence – challenges and opportunities for international HRM: A review and research agenda. *The International Journal of Human Resource Management, 33*(6), 1065–1097. https://doi.org/10.1080/09585192.2022.2035161

Budhwar, P. S., Varma, A., & Patel, C. (2016). Convergence-divergence of HRM in the Asia-Pacific: Context-specific analysis and future research agenda. *Human Resource Management Review, 26*(4), 311–326. https://doi.org/10.1016/j.hrmr.2016.04.004

Chowdhury, S., Budhwar, P., & Wood, G. (2024). Generative artificial intelligence in business: Towards a strategic human resource management framework. *British Journal of Management, 35*(4), 1680–1691. https://doi.org/10.1111/1467-8551.12824

Cooke, F. L. (2018). Concepts, contexts, and mindsets: Putting human resource management research in perspectives. *Human Resource Management Journal, 28*(1), 1–13. https://doi.org/10.1111/1748-8583.12163

De Cieri, H., Sanders, K., & Lin, C. (V.) (2022). International and comparative human resource management: An Asia-Pacific perspective. *Asia Pacific Journal of Human Resources, 60*(1), 116–145. https://doi.org/10.1111/1744-7941.12309

Demerouti, E., Bakker, A. B., Nachreiner, F., & Schaufeli, W. B. (2001). The job demands-resources model of burnout. *Journal of Applied Psychology, 86*(3), 499–512. https://doi.org/10.1037/0021-9010.86.3.499

Ehnert, I. (2009). *Sustainable human resource management: A conceptual and exploratory analysis from a paradox perspective*. Physica-Verlag. https://doi.org/10.1007/978-3-7908-2188-8

Frey, C. B., & Osborne, M. A. (2017). The future of employment: How susceptible are jobs to computerisation? *Technological Forecasting and Social Change, 114*, 254–280. https://doi.org/10.1016/j.techfore.2016.08.019

Hackman, J. R., & Oldham, G. R. (1976). Motivation through the design of work: Test of a theory. *Organizational Behavior and Human Performance, 16*(2), 250–279. https://doi.org/10.1016/0030-5073(76)90016-7

Hofstede, G. (2001). *Culture's consequences: Comparing values, behaviors, institutions, and organizations across nations* (2nd ed.). Sage.

Jaakkola, E. (2020). Designing conceptual articles: Four approaches. *AMS Review, 10*(1–2), 18–26. https://doi.org/10.1007/s13162-020-00161-0

Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at work: The new contested terrain of control. *Academy of Management Annals, 14*(1), 366–410. https://doi.org/10.5465/annals.2018.0174

Kramar, R. (2014). Beyond strategic human resource management: Is sustainable human resource management the next approach? *The International Journal of Human Resource Management, 25*(8), 1069–1089. https://doi.org/10.1080/09585192.2013.816863

Lebovitz, S., Lifshitz-Assaf, H., & Levina, N. (2022). To engage or not to engage with AI for critical judgments: How professionals deal with opacity when using AI for medical diagnosis. *Organization Science, 33*(1), 126–148. https://doi.org/10.1287/orsc.2021.1549

Lee, M., Coutts, R., Fielden, J., Hutchinson, M., Lakeman, R., Mathisen, B., Nasrawi, D., & Phillips, N. (2022). Occupational stress in university academics in Australia and New Zealand. *Journal of Higher Education Policy and Management, 44*(1), 57–71. https://doi.org/10.1080/1360080X.2021.1934246

Mah, D.-K., & Groß, N. (2024). Artificial intelligence in higher education: Exploring faculty use, self-efficacy, distinct profiles, and professional development needs. *International Journal of Educational Technology in Higher Education, 21*, Article 58. https://doi.org/10.1186/s41239-024-00490-1

Malik, A., Budhwar, P., & Kazmi, B. A. (2023). Artificial intelligence (AI)-assisted HRM: Towards an extended strategic framework. *Human Resource Management Review, 33*(1), Article 100940. https://doi.org/10.1016/j.hrmr.2022.100940

Meijerink, J., Boons, M., Keegan, A., & Marler, J. (2021). Algorithmic human resource management: Synthesizing developments and cross-disciplinary insights on digital HRM. *The International Journal of Human Resource Management, 32*(12), 2545–2562. https://doi.org/10.1080/09585192.2021.1925326

Morgeson, F. P., & Humphrey, S. E. (2006). The Work Design Questionnaire (WDQ): Developing and validating a comprehensive measure for assessing job design and the nature of work. *Journal of Applied Psychology, 91*(6), 1321–1339. https://doi.org/10.1037/0021-9010.91.6.1321

Nguyen, T. L. H. (2016). Building human resources management capacity for university research: The case at four leading Vietnamese universities. *Higher Education, 71*(2), 231–251. https://doi.org/10.1007/s10734-015-9898-2

Parker, S. K., & Grote, G. (2022). Automation, algorithms, and beyond: Why work design matters more than ever in a digital world. *Applied Psychology, 71*(4), 1171–1204. https://doi.org/10.1111/apps.12241

Prikshat, V., Malik, A., & Budhwar, P. (2023). AI-augmented HRM: Antecedents, assimilation and multilevel consequences. *Human Resource Management Review, 33*(1), Article 100860. https://doi.org/10.1016/j.hrmr.2021.100860

Raisch, S., & Krakowski, S. (2021). Artificial intelligence and management: The automation–augmentation paradox. *Academy of Management Review, 46*(1), 192–210. https://doi.org/10.5465/amr.2018.0072

Shoss, M. K. (2017). Job insecurity: An integrative review and agenda for future research. *Journal of Management, 43*(6), 1911–1939. https://doi.org/10.1177/0149206317691574

Sithambaram, R. A., & Tajudeen, F. P. (2023). Impact of artificial intelligence in human resource management: A qualitative study in the Malaysian context. *Asia Pacific Journal of Human Resources, 61*(4), 821–844. https://doi.org/10.1111/1744-7941.12356

Star, S. L., & Strauss, A. (1999). Layers of silence, arenas of voice: The ecology of visible and invisible work. *Computer Supported Cooperative Work, 8*(1–2), 9–30. https://doi.org/10.1023/A:1008651105359

Strich, F., Mayer, A.-S., & Fiedler, M. (2021). What do I do in a world of artificial intelligence? Investigating the impact of substitutive decision-making AI systems on employees' professional role identity. *Journal of the Association for Information Systems, 22*(2), 304–324. https://doi.org/10.17705/1jais.00663

Tarafdar, M., Cooper, C. L., & Stich, J.-F. (2019). The technostress trifecta – techno eustress, techno distress and design: Theoretical directions and an agenda for research. *Information Systems Journal, 29*(1), 6–42. https://doi.org/10.1111/isj.12169

Tarafdar, M., Tu, Q., Ragu-Nathan, B. S., & Ragu-Nathan, T. S. (2007). The impact of technostress on role stress and productivity. *Journal of Management Information Systems, 24*(1), 301–328. https://doi.org/10.2753/MIS0742-1222240109

Tims, M., Bakker, A. B., & Derks, D. (2012). Development and validation of the job crafting scale. *Journal of Vocational Behavior, 80*(1), 173–186. https://doi.org/10.1016/j.jvb.2011.05.009

Trist, E. L., & Bamforth, K. W. (1951). Some social and psychological consequences of the longwall method of coal-getting. *Human Relations, 4*(1), 3–38. https://doi.org/10.1177/001872675100400101

Vrontis, D., Christofi, M., Pereira, V., Tarba, S., Makrides, A., & Trichina, E. (2022). Artificial intelligence, robotics, advanced technologies and human resource management: A systematic review. *The International Journal of Human Resource Management, 33*(6), 1237–1266. https://doi.org/10.1080/09585192.2020.1871398

Watermeyer, R., Phipps, L., Lanclos, D., & Knight, C. (2024). Generative AI and the automating of academia. *Postdigital Science and Education, 6*(2), 446–466. https://doi.org/10.1007/s42438-023-00440-6

Whetten, D. A. (1989). What constitutes a theoretical contribution? *Academy of Management Review, 14*(4), 490–495. https://doi.org/10.5465/amr.1989.4308371

Wrzesniewski, A., & Dutton, J. E. (2001). Crafting a job: Revisioning employees as active crafters of their work. *Academy of Management Review, 26*(2), 179–201. https://doi.org/10.5465/amr.2001.4378011

Yan, L., Greiff, S., Lodge, J. M., & Gašević, D. (2025). Distinguishing performance gains from learning when using generative AI. *Nature Reviews Psychology, 4*(7), 435–436. https://doi.org/10.1038/s44159-025-00467-5
