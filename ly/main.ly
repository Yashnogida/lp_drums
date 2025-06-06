\version "2.24.4"

\paper {
  #(set-paper-size "letter")
  indent = 0.0
}

\header {  
    \include "title.ly"
    tagline = ""
}

\markup \vspace #1   % Space Between Title and first staff

\new DrumStaff <<
  \drummode {
    \include "time.ly"
    \include "notes.ly"
  }
>>

\layout {
  \context {
    \Staff \RemoveEmptyStaves
    \override VerticalAxisGroup.remove-first = ##t
  }
}