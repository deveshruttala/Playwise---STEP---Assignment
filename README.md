
# PlayWise Hackathon Submission Document

## Team/Student Details

- **Name**: Devesh Ruttala - RA2211027010133
- **Track**: DSA/Engineering Track
- **Project**: PlayWise - Smart Music Playlist Management Engine

---

## 1. High-Level Overview

PlayWise is a smart music playlist engine designed to provide personalized and dynamic user experiences through custom-built data structures. This backend CLI system allows users to manage playlists, playback history, rating systems, and song lookup in real-time with high performance and low memory usage.

---

## 2. Core Features Implemented

| Feature             | Data Structure Used      | Key Functions                                          |
| ------------------- | ------------------------ | ------------------------------------------------------ |
| Playlist Engine     | Doubly Linked List       | add\_song, delete\_song, move\_song, reverse\_playlist |
| Playback History    | Stack                    | add (push), undo\_last\_play (pop)                     |
| Song Rating Tree    | Binary Search Tree (BST) | insert\_song, search\_by\_rating                       |
| Instant Song Lookup | HashMap (Dict in Python) | add\_song, get\_metadata                               |
| Time-based Sorting  | Merge Sort               | sort\_by\_duration                                     |
| Dashboard Snapshot  | Mixed (Sort, Hash, Tree) | export\_snapshot                                       |

---

## 3. CLI User Interface

A menu-driven system has been built to allow users to:

- Add, delete, move, and reverse songs
- Play songs and undo playback
- View and sort playlist
- Rate songs and search by rating
- Retrieve metadata instantly
- View real-time snapshot (dashboard)

---

## 4. System Architecture Diagram

```
User Input
    |
    v
CLI Interface (main.py)
    |
    v
-------------------------------
| PlaylistEngine (LinkedList) |
| PlaybackHistory (Stack)     |
| SongRatingTree (BST)        |
| SongLookup (HashMap)        |
| Sorter (Merge Sort)         |
| Dashboard (Mixed DS)        |
-------------------------------
```

---

## 5. Time & Space Complexity (Key Functions)

| Function                   | Time Complexity | Space Complexity | Notes                                     |
| -------------------------- | --------------- | ---------------- | ----------------------------------------- |
| add\_song                  | O(1)            | O(1)             | Tail insert in doubly linked list         |
| delete\_song               | O(n)            | O(1)             | Linear traversal by index                 |
| move\_song                 | O(n)            | O(n)             | List reordering                           |
| reverse\_playlist          | O(n)            | O(1)             | Swapping pointers                         |
| undo\_last\_play           | O(1)            | O(1)             | Stack pop                                 |
| insert\_song (rating tree) | O(log n)        | O(log n)         | BST insert                                |
| search\_by\_rating         | O(log n)        | O(1)             | BST search                                |
| get\_metadata              | O(1)            | O(1)             | HashMap lookup                            |
| sort\_by\_duration         | O(n log n)      | O(n)             | Merge Sort                                |
| export\_snapshot           | O(n log n + r)  | O(n)             | Sort + Tree traversal (r = ratings depth) |

---

## 6. Sample Output (CLI Demo)

```bash
--- PlayWise CLI Menu ---
1. Add song to playlist
...
7. Show playlist
> Song A by Artist 1 (180s)
> Song B by Artist 2 (240s)
...
12. Show dashboard snapshot
> Top 5 Longest Songs: ['Song B (240s)', 'Song A (180s)', ...]
> Most Recently Played: ['Song A', 'Song B']
> Song Count by Rating: {5: 2, 4: 1}
```

---

## 7. Trade-Offs & Justification

- **Doubly Linked List** was chosen over arrays for O(1) insert/delete and ease of node swapping.
- **BST for Ratings** enables efficient range queries and ordering.
- **Stack for History** naturally supports LIFO undo operation.
- **HashMap** ensures O(1) access to metadata.
- **Merge Sort** provides stable, consistent sorting with guaranteed O(n log n).

---

## 8. Testing & Validation

Tested CLI interactions with valid/invalid inputs. Benchmarked sorting and lookup vs built-in Python features. Verified tree integrity with print and search methods.

---

## 9. Conclusion & Learnings

PlayWise is a complete backend CLI engine using custom data structures to solve real-world playlist challenges. This project demonstrates:

- Real-time playlist manipulation
- Personalized recommendations
- Efficient playback and metadata systems

Built fully from scratch, this system prepares for scaling to APIs or web integrations.

---

## 10. Appendix

- **main.py** — CLI Interface
- **playlist\_engine.py** — Linked List
- **playback\_history.py** — Stack
- **song\_rating\_tree.py** — BST
- **song\_lookup.py** — HashMap
- **sorting.py** — Merge Sort
- **dashboard.py** — Dashboard

