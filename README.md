# Truemed Interview Repo

## Next Steps
What was completed:
1. Call truemed api to get redirect url by passing as many values from the ui as possible
2. Truemed api returns redirect url
3. Load truemed UI
4. Upon completion on the truemed side, redirect back to checkout screen
5. Checkout screen should go to confirmation (I missed the part, where this was not required!)

What I would do next:
1. Confirm that the funds are actually being captured by truemed.
2. On the UI handle success and error paths. Likely using a combination of url params and local storage.
3. Create a cartId or something similar to pass as the `idempotency_key` to prevent creating an excessive number of payment sessions for the same cart.
4. Introduce some models on the api.
5. Add some validation and error handling.


## Senior Engineer

This project is meant to assess your ability to perform at a senior level at Truemed. Specifically, we expect senior developers to own large projects from end-to-end, even if some pieces are outside of your expertise. This often involves some research & planning before jumping straight to implementation (and course-correcting as you come across new information).

### Constraints

- Please don’t spend more than 3 hours on this project. We expect a barely-functional Proof-of-Concept and a write-up of next steps.

### Goal

Your mission is to implement the Truemed payment method on [this checkout page](https://www.loom.com/share/cde13fccd80543a7bb31ffe3b10e94c1?sid=f5d5af77-2605-42f2-8afd-e74fdd732c8f). Your priorities are:

P0 (most important):

- Get a Proof-of-Concept UX in place (redirect to Truemed for payment capture when a user presses the "Pay with HSA / FSA" button)

P1 (nice-to-have):

- Document next steps to improve the implementation

Out of Scope (don't do these, not even as a bonus):

- Any improvements to the store whatsoever
- Anything that requires a Django migration
- Order-confirmation logic

### How can I get started with the Truemed API?

- [Truemed developer docs](https://developers.truemed.com)
  - use `https://dev-api.truemed.com` as the base URL for our sandbox environment
- You should have an email with sandbox credentials

## Getting Started

- Create a personal, private fork of this repository
- Clone it locally
- Get the frontend & backend running (see readme files in each folder)

## Submission

It's important to make sure your submission is only visible to people with collaborator access to your private repo. Do not make a pull request against our main repository. Instead:

- Create a new branch (from your private fork's main branch) with your changes
- Create a Pull Request against your own fork's main branch
- Add `john@truemed.com` as an outside collaborator and email him a link to your Pull Request.

## FAQ

### What is this repository?

- A fork of [this project](https://github.com/kkosiba/ecommerce-backend?tab=readme-ov-file)
- Modified quickly to work as an interview starter project
- There are some...quirks (class-based React, UK currency & address validation, etc...)

### What are the expectations, exactly?

- Write great functions.
- Write a great plan for next steps.
- Don't refactor anything.

### What does a valid UK mailing address look like?

- https://chatgpt.com/share/bcd2d4e4-28e6-4db9-9081-5c02cb496e4a

### Where should I start writing code?

- `backend/payments/views.py`

### How should I handle secrets?

- Just hard-code all keys in `backend/src/settings/base.py`

### The backend project isn't reflecting my changes. What gives?

- This project doesn't have hot-reloading configured out of the box. The simplest workaround is to run `docker-compose build` when you make changes.

### Why is this repository so... bad?

- Truemed has high technical standards
- But we integrate with 1,000s of companies
- We need to meet our (mostly non-technical) partners where they're at.
