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

## Current status and next steps

- Review `Team3.pdf` using a readable version or accessible export and incorporate any additional requirements.
- Open the repository folder in VS Code and verify that **Research Ops Agent** appears and can be selected.
- Review the context and simulated research memory with the team before treating any hypothesis as validated.
- The context, research memory, agent, workflow log, and Copilot instruction are included in the requested `v0.0.1` commit.
