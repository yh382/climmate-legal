---
layout: default
title: Privacy Policy
permalink: /privacy/
---

# ClimMate Privacy Policy

**Last Updated: March 27, 2026**

ClimMate ("we," "us," or "our") operates the ClimMate mobile application (the "App"). This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you use our App.

By using ClimMate, you agree to the collection and use of information in accordance with this policy.

---

## 1. Information We Collect

### 1.1 Account Information

When you create an account, we collect:

- **Email address** — used for account login and recovery
- **Username** — a unique, public identifier you choose at registration
- **Display name** — your publicly visible name (can include any language)
- **Password** — stored only as a secure bcrypt hash; never stored in plain text

If you sign in with **Apple Sign In**, we receive your Apple user identifier and email address (which may be a private relay address if you choose to hide your email). We do not receive your Apple ID password.

### 1.2 Profile Information (Optional)

You may choose to provide additional profile information, including:

- **Bio and location** (city/region text)
- **Avatar and cover photo**
- **Physical attributes**: height, weight, ape index (wingspan)
- **Age and gender**
- **Fitness assessments**: strength metrics (pull-ups, hang time, grip strength), mobility scores
- **Training preferences**: training days per week, session duration, focus areas, injuries, available equipment

All profile fields beyond email and username are optional. Physical attributes are **private by default** and only visible to others if you explicitly change your privacy settings.

### 1.3 Training Data

When you use the App to track your climbing, we collect:

- **Climb logs**: date, wall type (boulder/lead/toprope/trad), grade, result (send/flash/onsight/attempt), feel rating, style tags, attempt count, notes
- **Climb sessions**: date, start/end time, duration, location (gym name or outdoor area), session notes and summary
- **Training plans**: plan title, structure, schedule, type, and completion progress
- **Performance statistics**: aggregated from your logs (e.g., send rates, grade progression)

### 1.4 Location Data

- **GPS location** (with your permission): used to find nearby climbing gyms on the map. Your real-time GPS coordinates are sent to our server to query nearby gyms but are **not** stored as location history.
- **Home gym**: if you set a home gym, we store the gym name and its coordinates.
- **Stated location**: if you add a city/region to your profile, we store the text and coordinates.
- **Per-session gym**: each climbing session may be associated with a gym.

You can deny location permission and still use the App — you will need to search for gyms manually.

### 1.5 Social & Community Data

If you use ClimMate's social features, we collect:

- **Posts and comments** you create, including any attached media or training data
- **Follows**: who you follow and who follows you
- **Blocks**: users you have blocked
- **Mentions**: when you @mention other users
- **Likes and saves**: content you have liked or bookmarked
- **Direct messages**: message text between you and other users, including read status
- **Content views**: which posts you viewed and from what source (feed, search, or direct link)
- **Reports**: if you report content, we store the report reason and resolution

### 1.6 AI Coaching Data

ClimMate offers an AI-powered coaching feature. When you use it:

- Your climbing history, profile data, and chat messages are sent to our AI service provider (OpenAI) to generate personalized coaching responses.
- Your AI coaching conversation history is stored on our servers.

### 1.7 Media

- **Photos**: avatar, cover photo, and media attached to climb logs or posts are uploaded to our cloud storage (Cloudflare R2).
- We request camera and photo library permissions only when you choose to upload a photo.

### 1.8 Device & Technical Data

- **Push notification token**: if you enable notifications, we store your device's push token to deliver notifications via Expo Push Notification service.
- **Device platform**: iOS or Android, used to format push notifications correctly.
- **App preferences**: language, unit system (metric/imperial), and grade scale preferences are stored **locally on your device only** and are not sent to our servers.
- **Authentication tokens**: JWT tokens are stored in your device's secure enclave (iOS Keychain / Android Keystore) and are never shared.

### 1.9 Information We Do NOT Collect

- We do not use any third-party analytics or tracking SDKs (no Google Analytics, Firebase Analytics, Amplitude, Mixpanel, etc.)
- We do not collect device advertising identifiers (IDFA/GAID)
- We do not track your browsing activity outside the App
- We do not sell your data to any third party

---

## 2. How We Use Your Information

We use the information we collect to:

| Purpose | Data Used |
|---|---|
| Provide and maintain the App | Account info, training data |
| Authenticate your identity | Email, password hash, Apple Sign In ID |
| Display your public profile | Username, display name, avatar, bio |
| Track your climbing progress | Climb logs, sessions, plans |
| Show nearby climbing gyms | GPS location (session-only) |
| Enable social features | Posts, comments, follows, messages |
| Deliver push notifications | Push token, notification preferences |
| Provide AI coaching | Profile, climb history, chat messages |
| Compute rankings and badges | Training data, aggregated stats |
| Enforce community guidelines | Reports, blocks, content moderation |

---

## 3. How We Share Your Information

We do **not** sell, rent, or trade your personal information. We share data only in these limited circumstances:

### 3.1 Third-Party Service Providers

| Provider | Purpose | Data Shared |
|---|---|---|
| **Apple** | Sign In with Apple authentication | Your Apple user ID is verified with Apple's servers |
| **Google (Places API)** | Gym discovery | Your approximate location (lat/lng) is sent to Google to find nearby gyms |
| **Mapbox** | Map rendering | Your device loads map tiles from Mapbox; your location is not sent to Mapbox by us |
| **Cloudflare (R2)** | Photo storage | Photos you upload are stored on Cloudflare's infrastructure |
| **OpenAI** | AI coaching | Your climbing profile, history, and coaching chat messages are processed by OpenAI |
| **Expo** | Push notifications & app updates | Your push token is sent through Expo's push notification service |

Each provider is bound by their own privacy policy and data processing terms.

### 3.2 Other Users

Depending on your privacy settings, other ClimMate users may see:

- Your username, display name, avatar, and bio (always public)
- Your posts and comments (based on your visibility setting: public, followers-only, or private)
- Your climb logs and sessions (if you set them to public)
- Your training plans (if you set them to public)
- Your badges and rank (configurable in privacy settings)
- Your physical attributes (private by default; opt-in to share)

### 3.3 Legal Requirements

We may disclose your information if required to do so by law or in response to valid legal process (e.g., a court order or subpoena).

---

## 4. Data Storage and Security

- **Server location**: Your data is stored on our servers using PostgreSQL databases with encryption at rest.
- **Passwords**: Stored as bcrypt hashes — we never store or have access to your plain-text password.
- **Auth tokens**: Access tokens (60-minute expiry) and refresh tokens (60-day expiry) are stored in your device's hardware-backed secure storage (iOS Keychain / Android Keystore).
- **Token rotation**: Refresh tokens are rotated on each use. Old tokens are invalidated to prevent replay attacks.
- **Photos**: Uploaded via presigned URLs directly to Cloudflare R2 over HTTPS.
- **Transport**: All communication between the App and our servers uses HTTPS/TLS encryption.

While we implement industry-standard security measures, no method of electronic storage or transmission is 100% secure. We cannot guarantee absolute security.

---

## 5. Data Retention

- **Account data**: Retained as long as your account is active.
- **Training data**: Retained as long as your account is active. You can delete individual logs and sessions at any time.
- **Messages**: Retained as long as the conversation exists. You can delete conversations.
- **AI coaching history**: Retained as long as your account is active.

When you delete your account, all associated personal data is permanently deleted from our servers within 30 days, except where retention is required by law.

---

## 6. Your Rights and Choices

### 6.1 Access and Portability

You can view all your personal data within the App (profile, logs, sessions, plans, messages).

### 6.2 Correction

You can update your profile information, display name, and other details at any time through the App.

### 6.3 Deletion

You can:

- Delete individual climb logs, sessions, posts, and messages within the App
- **Delete your entire account** from the Settings page, which permanently removes all your data

### 6.4 Privacy Controls

You can configure visibility for:

- Posts (public / followers-only / private)
- Climb logs and sessions (public / private)
- Training plans (public / private)
- Physical attributes (private by default)
- Analysis data, badges, and rank

### 6.5 Notification Preferences

You can choose which types of push notifications to receive (likes, comments, follows, mentions, challenges, events) or disable them entirely.

### 6.6 Location Permission

You can revoke location permission at any time through your device settings. The App will continue to function — you will search for gyms by name instead of proximity.

---

## 7. Children's Privacy

ClimMate is not intended for children under the age of 13 (or the applicable age of digital consent in your jurisdiction). We do not knowingly collect personal information from children under 13. If you believe a child under 13 has provided us with personal information, please contact us and we will delete it.

---

## 8. International Data Transfers

Your information may be transferred to and processed in countries other than your country of residence. These countries may have different data protection laws. By using the App, you consent to the transfer of your information to these countries. We take steps to ensure your data is treated securely and in accordance with this Privacy Policy.

---

## 9. Changes to This Privacy Policy

We may update this Privacy Policy from time to time. We will notify you of any material changes by:

- Posting the updated policy within the App
- Updating the "Last Updated" date at the top of this document

Your continued use of the App after changes are posted constitutes acceptance of the updated policy.

---

## 10. Contact Us

If you have questions about this Privacy Policy or wish to exercise your data rights, please contact us at:

**Email**: [privacy@climmatestudio.com]

---

*This privacy policy applies to the ClimMate mobile application and associated services.*
