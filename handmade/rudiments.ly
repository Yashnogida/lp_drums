\version "2.24.4"

\paper {
  indent = 0.0
}

\header {  
    title = "Paradiddles"
    tagline = ""
}

\markup \vspace #1   % Space Between Title and first staff

\new RhythmicStaff { 
  
  \time 2/4

  c16^"R" c16^"L" c16^"R" c16^"R" c16^"L" c16^"R" c16^"L" c16^"L"
  c16^"L" c16^"R" c16^"L" c16^"R" c16^"R" c16^"L" c16^"R" c16^"L"
  c16^"L" c16^"L" c16^"R" c16^"L" c16^"R" c16^"R" c16^"L" c16^"R"
  c16^"R" c16^"L" c16^"L" c16^"R" c16^"L" c16^"R" c16^"R" c16^"L"
  c16^"L" c16^"R" c16^"L" c16^"L" c16^"R" c16^"L" c16^"R" c16^"R"
  c16^"R" c16^"L" c16^"R" c16^"L" c16^"L" c16^"R" c16^"L" c16^"R"
  c16^"R" c16^"R" c16^"L" c16^"R" c16^"L" c16^"L" c16^"R" c16^"L"
  c16^"L" c16^"R" c16^"R" c16^"L" c16^"R" c16^"L" c16^"L" c16^"R"
}


\markup \vspace #1   % Space Between Title and first staff

\new RhythmicStaff { 

  \time 2/4

  \tuplet 3/2 {c8^"R" c8^"L" c8^"L"}  \tuplet 3/2 {c8^"R" c8^"R" c8^"L"}
  \tuplet 3/2 {c8^"L" c8^"R" c8^"L"}  \tuplet 3/2 {c8^"L" c8^"R" c8^"R"}
  \tuplet 3/2 {c8^"R" c8^"L" c8^"R"}  \tuplet 3/2 {c8^"L" c8^"L" c8^"R"}
  \tuplet 3/2 {c8^"R" c8^"R" c8^"L"}  \tuplet 3/2 {c8^"R" c8^"L" c8^"L"}
  \tuplet 3/2 {c8^"L" c8^"R" c8^"R"}  \tuplet 3/2 {c8^"L" c8^"R" c8^"L"}
  \tuplet 3/2 {c8^"L" c8^"L" c8^"R"}  \tuplet 3/2 {c8^"R" c8^"L" c8^"R"}
}

\layout {
  \context {
    \RhythmicStaff \RemoveEmptyStaves
    \override VerticalAxisGroup.remove-first = ##t
  }
}

