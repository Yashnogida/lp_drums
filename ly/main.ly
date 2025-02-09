\version "2.24.4"

\paper {
  indent = 0.0
}

\header {  
    \include "title.ly"
    tagline = ""
}

\markup \vspace #1   % Space Between Title and first staff

notes = \relative c' {
  \time 2/4
  \fixed c''
  {
    \clef treble
    \include "notes.ly"
  }
}


\new Staff{ 
    \notes 
}


\layout {
  \context {
    \Staff \RemoveEmptyStaves
    \override VerticalAxisGroup.remove-first = ##t
  }
}