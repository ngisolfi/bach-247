"""Channel line-up for Bach 24/7. Edit here to change channels; both scripts read it."""

# The Netherlands Bach Society's own YouTube playlists that feed the channels.
PLAYLISTS = {
    "cantatas": "PLecKPCyj4yRMxTujJw1hSwtFK0-KiUTx1",
    "organ": "PLecKPCyj4yRNiUAVGJ6xRW7ZnVJOBLiLp",
    "harpsichord": "PLecKPCyj4yRO_h8ZTj6UX9eNw8_bwKuwh",
    "chamber": "PLecKPCyj4yRNYD46FdcP4o045xyhW_1oV",
    "cello": "PLecKPCyj4yROEWW268aqNqgeo0tiehjZf",
    "violinsolo": "PLecKPCyj4yRP8P_v2XXxP85CGaXxs4LWw",
    "orchestral": "PLecKPCyj4yROflt6ofNYNPTlWavQRnncS",
    "violinconc": "PLecKPCyj4yROhtiMi5e_GMjpD35etUTS9",
    "brandenburg": "PLecKPCyj4yRPbITUktWxsBqLgwTuPPfEq",
    "oratorios": "PLecKPCyj4yROmFhJRbmE7A-1QSj5VRnIY",
    "latin": "PLecKPCyj4yRNpIga30JFd7ed_4Fb2Te7_",
    "motets": "PLecKPCyj4yRNYXUCiwRh9cLj-T3c71upX",
    "songs": "PLecKPCyj4yRM6JKkc2oXIR5zPS3fgV0uj",
    "chorales": "PLecKPCyj4yROJa5qy_tNwT8_c6jhXyLX-",
    "complete": "PLecKPCyj4yRO-qy4suHUdmYJTw615diKt",
}

# Recordings missing from every genre playlist, filed by hand (skipped if no longer available).
EXTRA = {
    "harpsichord": ["FAdzfW604e0", "HrpzQEv-eos", "irneC1jhpqg", "QIveGkUw2FI"],
    "chamber": ["N6sUlZa-IrU"],
}

# (key, name, playlists). The guide shows channels in this order; "*" means every recording.
CHANNELS = [
    ("cantatas", "Cantatas", ["cantatas"]),
    ("organ", "Organ", ["organ"]),
    ("keyboard", "Harpsichord", ["harpsichord"]),
    ("chamber", "Chamber & solo", ["chamber", "cello", "violinsolo"]),
    ("orchestral", "Orchestral", ["orchestral", "violinconc", "brandenburg"]),
    ("sacred", "Passions & Masses", ["oratorios", "latin", "motets"]),
    ("songs", "Songs & chorales", ["songs", "chorales"]),
    ("all", "All of Bach", "*"),
]
