# Contributing: Adding a New Skill

This guide is for Stefanos and CAIO team members maintaining this repo.

## Adding a Skill

1. Create a folder under `skills/` with a lowercase, hyphenated name
2. Include at minimum a `SKILL.md` with proper YAML frontmatter:
   ```yaml
   ---
   name: your-skill-name
   description: >
     One paragraph describing what the skill does and when it triggers.
   ---
   ```
3. Add a `README.md` with a human-readable explanation, installation notes, and usage examples
4. Place any reference files in a `references/` subfolder
5. Update the main `README.md`:
   - Add a row to the **Skills Catalog** table
   - Add a new section under **Skill Showcase**

## Folder Structure

```
skills/your-skill-name/
├── SKILL.md              ← Required. The skill definition Claude reads.
├── README.md             ← Required. Human-readable documentation.
└── references/           ← Optional. Supporting files the skill needs.
    └── example.md
```

## Naming Conventions

- Folder names: lowercase, hyphenated (e.g., `the-sun-tzu-lens`)
- SKILL.md `name` field: must match the folder name
- Keep names descriptive but concise

## Quality Checklist

Before pushing:

- [ ] SKILL.md has valid YAML frontmatter with `name` and `description`
- [ ] Description includes trigger phrases and use cases
- [ ] README.md explains what the skill does, how to use it, and how to install it
- [ ] All referenced files exist in the correct paths
- [ ] Main README.md catalog table and showcase section are updated
- [ ] Tested the skill in at least one environment (Projects or Cowork)
