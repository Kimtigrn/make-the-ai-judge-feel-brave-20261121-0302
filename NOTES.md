# Notes — make-the-ai-judge-feel-brave-20261121-0302

Entry: a program (`main.py`, Python 3.13 stdlib only, no network) that writes
one 256-character text to `/output/entry.txt`.

## The text

> Rain on the roof, one drop at a time, each finding the same dark shingle.
> The kettle ticks as it cools. Steam rises, thins, and is gone, and the
> room stays warm anyway. Nothing here is in a hurry. The road will still
> be there when you are ready to walk it.

## Design against the judge brief

1. **Relaxes first:** slow rhythm, rain and a cooling kettle — reading it
   slows the reader down instead of winding them up.
2. **Courage shown, not instructed:** no imperatives anywhere. Readiness
   arrives as a fact ("the road will still be there"), not a command.
3. **Craft:** plain, concrete, gentle words; nothing that could be cut.
   The commas pace the reading ("rises, thins, and is gone").
4. **Lingers:** two images keep working after the last line — steam gone
   but the room still warm; a road waiting for the reader's feet.
5. **Freshness:** specific images (the same dark shingle, the kettle
   ticking as it cools) instead of stock wellness phrases or a meditation
   script. No "breathe", no "let go", no "you are enough".

## Status

- Repo created 2026-11-21 (after the competition opened 03:02Z): public,
  MIT license, README badges + About set from the requirements API.
- Local test: `python3 main.py` writes `/output/entry.txt`, 256 code
  points, UTF-8, deterministic across runs.
- SUBMIT PENDING: the kit CLI step (bundle / check / submit) is BLOCKED by
  a platform execution-risk flag on the downloaded kit tarball — see
  HANDOFF.md. Bundle + submit must run from inside a git clone of this
  repo once the Boss gives a plain-words go-ahead for processing the kit.
