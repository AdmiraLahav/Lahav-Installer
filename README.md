# My installer
Cloner.py - clones a repo from a link and opens explorer on that folder

# Action Tree

- Start
  - Validate input
    - If valid
      - Load config
      - Execute main routine
        - Success
          - Log result
          - Exit 0
        - Failure
          - Handle error
          - Exit 1
    - If invalid
      - Show error
      - Exit 1
