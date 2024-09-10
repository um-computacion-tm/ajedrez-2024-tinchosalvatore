# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## V[1.0] - 2024-08-27

### Added

- v1.0 Functional Chess, but pieces especial behavior is not done 

### Fixed
-How board was initialized
-How pieces understand their positions in the board

### Changed
- Changed most of the structural problems of the code that doesnt respect the SOLID principles

## V[1.1] - 2024-09-04

### Added

Added the special behavior of every piece, but the match doesnt finish and the code isnt completely tested

### Fixed
- Fixed pawn movement that was broken
- Fixed king movement that wasnt limited to one square

### Changed
- Changed how general pieces movement was done, by adding a new general method for them

## V[1.2] - 2024-09-09
### Added

Killing the king finishes the match

### Fixed
- Fixed queen movement that wasnt able to do diagonal moves
- Fixed pawns, now they cant capture pieces in vertical