# EcoEdu MVP

A web-first MVP for a Gamified Environmental Education Platform.

## Quick start

1. Copy env

2. Start services

3. Install deps and run dev


## Features
- Role-based auth (students, teachers, citizens)
- Mongo models for users, groups, modules, assignments, submissions, posts, gamification
- REST-style API routes for users, groups, modules, posts, leaderboard
- Basic dashboards and eco-feed with upload
- Gamification stubs (points, streaks)
- Verification queue (mock) via BullMQ + Redis

## Tech
- Next.js App Router, TypeScript, Tailwind CSS
- MongoDB (Docker), Redis (Docker)
- NextAuth credentials provider
- Mongoose, Zod, BullMQ

## Notes
- AI verification is mocked; integrate OpenCV/TensorFlow behind the queue worker later.
- Add proper storage (Cloudinary/Firebase Storage) for media in production.
