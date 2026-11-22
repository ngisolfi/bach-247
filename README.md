# Bach 24/7

Eight always-on channels of Netherlands Bach Society recordings from their free [All of Bach](https://www.bachvereniging.nl/en/allofbach) project, played through YouTube's official embedded player.

**Open it:** https://ngisolfi.github.io/bach-247/

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

Each channel runs on a broadcast clock that started on 1 January 2026 (UTC), and every loop through a channel plays in a new shuffled order. When you tune in, the page works out what that channel is playing *right now* and joins the piece partway through, like Criterion 24/7. Come back an hour later and the channel has moved on an hour. The guide shows what's on and what's next for every channel.

No server runs the channels. Every copy of the page does the same arithmetic from the same clock, catalogue and shuffle, so everyone who opens it sees the same piece at about the same point. If a video starts late or in the wrong place (after an ad, after tapping to start it, after a pause, or when you return to the app), the page jumps to the scheduled point, like live TV. If you tune in during a piece's first 20 seconds, it starts from the beginning so you don't miss the opening.

YouTube may show ads before a piece. If a video doesn't start on its own, a small hint appears at the bottom: tap the video to start it.

## Controls

**On a phone or tablet**
- Tap a channel in the guide to tune in
- One-finger tap on the picture: what's playing, with **Mute** and **Guide** buttons
- Two-finger tap: channel guide
- Swipe left or right: change channel

**On a computer**
- Click the picture: channel guide
- `↑` `↓` choose a channel, `Enter` tune in
- `←` `→` or `1`–`8` change channel
- `G` guide, `I` what's playing, `M` mute, `Space` pause, `F` full screen

The page remembers your last channel. Browsers only play sound after you've tapped or clicked once, so the first channel each time is picked by hand.

## Add it to your iPhone home screen

1. On the iPhone, open **Safari** and go to **ngisolfi.github.io/bach-247**.
2. Tap the **Share** button (the square with an arrow pointing up). It's at the bottom of the screen on iPhone, or the top on iPad.
3. Scroll down and tap **Add to Home Screen**. If it isn't listed, tap **Edit Actions** at the bottom of the menu and add it.
4. Check the name reads **Bach 24/7** and tap **Add**.

The Bach 24/7 icon appears on your home screen and opens full screen, without Safari's address bar. After the site changes, close the app completely and open it again to get the new version.

## Watch on an Apple TV

Open the page on an iPhone, iPad or Mac, tune in, then use **Control Center → Screen Mirroring** and choose your Apple TV. On a Mac, "Use as separate display" lets you drag Safari onto the TV and press `F` for full screen. The channels run on whichever device has the page open, so keep that device awake.

## Keeping the catalogue current

The Bach Society releases a new recording roughly every two weeks. The channels use a snapshot of their YouTube genre playlists taken on 22 November 2026. To refresh it, ask Claude to re-collect the playlists and rebuild `index.html`.
