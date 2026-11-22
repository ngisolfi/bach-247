# Bach 24/7

Eight always-on channels of Netherlands Bach Society recordings (All of Bach), played through YouTube's official embedded player.

| # | Channel | Recordings | Loop length |
|---|---------|-----------:|------------:|
| 1 | Cantatas | 108 | 36 h |
| 2 | Organ | 143 | 14 h |
| 3 | Harpsichord | 138 | 20 h |
| 4 | Chamber & solo (incl. cello suites, solo violin) | 57 | 13 h |
| 5 | Orchestral (incl. Brandenburgs, violin concertos) | 28 | 7 h |
| 6 | Passions & Masses (oratorios, Latin works, motets) | 20 | 12 h |
| 7 | Songs & chorales | 54 | 3 h |
| 8 | All of Bach | 539 | 104 h |

## How it behaves

Each channel runs on a broadcast clock that started on 1 Jan 2026. Every loop through a channel is shuffled into a new order. When you open the page, it works out what each channel is playing *right now* and joins that piece partway through, like Criterion 24/7. If you close the page and come back an hour later, the channel has moved on an hour. The guide shows what's on and what's next for every channel.

Controls (keyboard, or click anywhere to open the guide):
- `↑` `↓` choose a channel, `Enter` tune in
- `←` `→` or `1`–`8` change channel
- `G` guide, `I` what's playing, `F` full screen, `M` mute, `Space` pause

The page remembers your last channel. Browsers block sound until you click once, so the first channel always has to be picked by hand.

## Running it

YouTube refuses to play from a file you double-click (`file://`), so the page has to be served over http. You have two options:

**A. On your Mac (quickest).** Double-click `serve.command`. It starts a small local server, opens Safari, and keeps the Mac awake until you close the Terminal window. The first time, macOS may block it: right-click it and choose Open. If it says `python3` is missing, run `xcode-select --install` once.

**B. Free hosting on GitHub Pages (works from any device).** Create a repository, upload `index.html`, then go to Settings → Pages → Deploy from branch `main`. The page will be live at `https://<you>.github.io/<repo>/`, and you can open it from an iPhone or iPad too.

## Getting it onto the Apple TV

- **From the Mac:** Control Center → Screen Mirroring → your Apple TV. Choose "Use as separate display", drag Safari onto the TV screen, and press `F`.
- **From an iPhone or iPad:** open the hosted page (option B) in Safari, pick a channel, then Control Center → Screen Mirroring.

The schedule runs on whichever device has the page open, so that device needs to stay awake.

## Keeping the catalogue current

The Bach Society releases a new recording roughly every two weeks. The channels use a snapshot of their YouTube genre playlists from 22 Nov 2026. To refresh it, ask Claude to re-collect the playlists and rebuild `index.html`.
