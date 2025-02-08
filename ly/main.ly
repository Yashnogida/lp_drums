\version "2.24.4"

\paper {
  indent = 0.0
}

\header {  
    title = "Kick Doubles 16th Notes"
    tagline = ""
}

\markup \vspace #1   % Space Between Title and first staff

notes = \relative c' {
  \time 2/4
  \include "notes.ly"
}


\new Staff{ 
    \notes 
}


\layout {
  \context {
    \Staff \RemoveEmptyStaves
    % To use the setting globally, uncomment the following line:
    \override VerticalAxisGroup.remove-first = ##t
  }
}