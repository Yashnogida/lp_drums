\version "2.24.4"

\paper {
  #(set-paper-size "letter")
  indent = 0.0
}

\markup \vspace #1   % Space Between Title and first staff

\include "staff.ly"

\layout {
  \context {
    \Staff \RemoveEmptyStaves
    \override VerticalAxisGroup.remove-first = ##t
  }
}