# Nikolay's workflow

This is the ongoing project workflow log. The Copilot assistant acts as orchestrator: record project discussions, decisions, completed work, open questions, and next steps here. Keep entries factual and identify limitations; do not record credentials, private interview data, or sensitive personal information.

The research evidence and its validation status belong in [research-memory.md](research-memory.md); the stable project brief belongs in [context.md](context.md).

## 2026-11-23

### Repository setup

- Created the `Independent Living` subfolder and initialized a Git repository on `main`.
- Added a README containing only the title "Independent Living" and pushed the initial commit to [GitHub](https://github.com/djnizzi/Independent-Living).

### Sources and project context

- Confirmed Figma MCP access and inspected the **Cover** page.
- Read the available text metadata from [01. Brainstorming Azzurra](https://www.figma.com/design/XPH6H7C0SX9qvFE0pZPRye/Independent-Living----Eng?node-id=9-3): the challenge, research approach, example prompts, service directions, consent, and measurement guidance.
- Read `Independent_Living_Research_Kit.docx`: the research cycle, simulated interviews, proto-personas, journey, user stories, shared memory, agent prompt, and metrics.
- Attempted to read `Team3.pdf`, but its contents could not be reliably extracted or rendered. **The PDF has not been reviewed**; its requirements remain to be checked.
- Created [context.md](context.md) and [research-memory.md](research-memory.md). The initial interviews and personas are simulated and must not be presented as real research.

### Research Ops Agent

- Created the [Research Ops Agent](.github/agents/research-ops-agent.agent.md) as a Copilot custom agent. Its role is to support the UX team with evidence-linked research, while the designer validates insights.
- Explained how to activate it: open the `Independent Living` folder as the VS Code workspace, start a Copilot chat, and select **Research Ops Agent** from the Agent dropdown. Check **Chat: Open Customizations** if it is missing. Activation has not yet been verified.

### Orchestration and workflow tracking

- The user requested that the Copilot assistant act as orchestrator and keep this file updated with project discussions and work.
- Created this log and a repository-wide Copilot instruction to prompt future sessions to maintain it.
- The user requested a commit and push tagged `v0.0.1` for the project setup files.

### Agent revision requested

- Claude examined `v0.0.1` and proposed improvements; the designer asked Copilot to implement them after review and confirmation.
- The designer approved the proposed changes, separate agent/project versioning, a `v0.1.0` Git tag, the citation-checker conventions, and this workflow update.
- The designer retained ownership of insight validation and the metrics baseline. `context.md` and `research-memory.md` must not be modified without permission.
- Implemented the eight logical changes in the requested order, including synthetic adversarial fixtures and citation-checker tests. The checker tests use only synthetic fixture material; the three agent-behavior scenarios still need to be run and reviewed with the designer.

## 2026-11-24

### Agent picker and agent assessment

- The designer found the **Research Ops Agent** in the GitHub Copilot app's agent picker. The agent was not yet run on a task.
- Copilot assessed the agent as strong on evidence discipline, designer control, and ethics. Noted weaknesses: mixed English/Italian rules, a long mandatory start-up read, agent version `0.2` versus project tag `v0.1.0`, "Breve" mode skipping metrics, and the checker not verifying meaning. Scenarios T1–T3 have not been run.

### Team3.pdf reviewed

- `Team3.pdf` (parent folder, 4 image-only slides) was read by rendering the pages; text extraction does not work.
- Content: Brief 3/6, client Bticino/Riello. Question: how can a person over 70 live independently without feeling controlled? Challenge: an agentic experience that supports, and does not replace, the person's choices. Constraint: the client requires an **optional** caregiver-involvement mode.
- Asset to build: Research Ops Agent (prepares the protocol, synthesizes interviews and tests, keeps the needs map for older adults and caregivers). Metrics: time from protocol to synthesis, source-traceable insights, human revisions. The designer checks syntheses and decides what is an insight, starting from perceived control. Integration options: GitHub Copilot, Eng Code, Figma; Open Claw or GitHub agent libraries as starting points.
- Slide 4 is a team page; roles, super powers, and team name are blank.
- Observed fit: the agent matches the brief. It does not mention the client or the Eng Code/Figma integrations. `context.md` and `research-memory.md` were not changed; whether to add the client and optional-caregiver constraint is for the designer to decide.

## Current status and next steps

- `context.md` was updated at the designer's request (2026-11-24): the PDF is now listed as reviewed and a "Client brief" section records the client, challenge, optional-caregiver constraint, asset, metrics, and designer role. `research-memory.md` was not changed.
- Run scenarios T1–T3 with the Research Ops Agent and review the results with the designer.
- Review the context and simulated research memory with the team before treating any hypothesis as validated.
- The context, research memory, agent, workflow log, and Copilot instruction are included in the requested `v0.0.1` commit.
