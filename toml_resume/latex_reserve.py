start = r"""\documentclass[12pt]{article}
\usepackage[cm]{fullpage}
\usepackage{hyperref}
\usepackage{fontawesome}
\usepackage{amssymb}
\usepackage[b4paper, paperwidth=9in, paperheight=12.2in, margin=0.3in]{geometry}
\usepackage{lmodern}
\usepackage[usenames,dvipsnames]{color}
\usepackage{enumitem}

\hypersetup{breaklinks=true,%
pagecolor=white,%
colorlinks=true,%
linkcolor=cyan,%
urlcolor=MyLinkColor}

\definecolor{MyDarkBlue}{rgb}{0,0.0,0.45}
\definecolor{MyLinkColor}{rgb}{0,0.208,0.459}
\renewcommand{\familydefault}{\sfdefault}

%%%%%%%%%%%%%%%%%%%%%%%%%%
% Formatting parameters  %
%%%%%%%%%%%%%%%%%%%%%%%%%%

\newlength{\tabin}
\setlength{\tabin}{1em}
\newlength{\secsep}
\setlength{\secsep}{0.1cm}

\setlength{\parindent}{0in}
\setlength{\parskip}{0in}
\setlength{\itemsep}{0in}
\setlength{\topsep}{0in}
\setlength{\tabcolsep}{0in}

\definecolor{contactgray}{gray}{0.3}

\definecolor{darkblue}{rgb}{0.0, 0.0, 0.55}

\pagestyle{empty}

%%%%%%%%%%%%%%%%%%%%%%%%%%
%  Template Definitions  %
%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\lineunder}{\vspace*{-8pt} \\ \hspace*{-6pt} \hrulefill \\ \vspace*{-15pt}}
\newcommand{\name}[1]{\begin{center}\textsc{\color{darkblue}\Huge#1}\end{center}}
\newcommand{\program}[1]{\begin{center}\textsc{#1}\end{center}}
\newcommand{\contact}[1]{\begin{center}{\small#1}\end{center}}

\newenvironment{tabbedsection}[1]{
  \begin{list}{}{
      \setlength{\itemsep}{0pt}
      \setlength{\labelsep}{0pt}
      \setlength{\labelwidth}{0pt}
      \setlength{\leftmargin}{3pt}
      \setlength{\rightmargin}{5pt}
      \setlength{\listparindent}{0pt}
      \setlength{\parsep}{0pt}
      \setlength{\parskip}{0pt}
      \setlength{\partopsep}{0pt}
      \setlength{\topsep}{#1}
    }
  \item[]
}{\end{list}}

\newenvironment{nospacetabbing}{\begin{tabbing}}
{\end{tabbing}\vspace{-1.2em}}

\newenvironment{resume_header}{}{\vspace{2pt}}

\newenvironment{resume_section}[1]{
  \filbreak
  \vspace{2\secsep}
  \textbf{\color{YellowOrange}\Large#1 \hrulefill } \textcolor{white}{\lineunder} \vspace{-7pt}
  \begin{tabbedsection}{\secsep}
}{\end{tabbedsection}}

\newenvironment{resume_subsection}[2][]{
  \vspace{\secsep}
  \textbf{#2} \hfill {\small #1} %\hspace{2em}
  \vspace{2 pt}
  \begin{tabbedsection}{0.5\secsep}
}{\end{tabbedsection}}

\newenvironment{education}[3][]{
  \vspace{\secsep}
  \textbf{#2} \hfill {\hspace{-2pt} #3}\\
  \vspace{-13pt}
  \begin{tabbedsection}{\secsep}
}{\end{tabbedsection}}

\newenvironment{subitems}{
  \renewcommand{\labelitemi}{-}
  \begin{itemize}
      \setlength{\labelsep}{0.7em}
}{\end{itemize}}

\newenvironment{nobulletsubitems}{
  \renewcommand{\labelitemi}{} % Remove bullet point
  \begin{itemize}[leftmargin=*]
}{\end{itemize}}

\newenvironment{resume_employer}[4]{
  \vspace{\secsep}
  \textbf{#1} \hfill  {\color{YellowOrange} \footnotesize#3 \vspace{1 pt}}\\ 
  \normalsize{\it #2} \hfill { \footnotesize {#4}} \\
  \vspace{-15 pt} 
  \begin{tabbedsection}{0pt}
  \vspace{1.5pt}
  \begin{subitems}
}{\end{subitems}\end{tabbedsection} \vspace{4pt}}

\begin{document}
"""

grayscale_start = r"""\documentclass[12pt]{article}
\usepackage[cm]{fullpage}
\usepackage{hyperref}
\usepackage{fontawesome}
\usepackage{amssymb}
\usepackage[b4paper, paperwidth=9in, paperheight=12.2in, margin=0.3in]{geometry}
\usepackage{lmodern}
\usepackage[usenames,dvipsnames]{color}
\usepackage{enumitem}

\hypersetup{breaklinks=true,%
pagecolor=white,%
colorlinks=true,%
linkcolor=cyan,%
urlcolor=MyLinkColor}

\definecolor{MyDarkBlue}{rgb}{0,0.0,0.45}
\definecolor{MyLinkColor}{rgb}{0,0.208,0.459}
\renewcommand{\familydefault}{\sfdefault}

%%%%%%%%%%%%%%%%%%%%%%%%%%
% Formatting parameters  %
%%%%%%%%%%%%%%%%%%%%%%%%%%

\newlength{\tabin}
\setlength{\tabin}{1em}
\newlength{\secsep}
\setlength{\secsep}{0.1cm}

\setlength{\parindent}{0in}
\setlength{\parskip}{0in}
\setlength{\itemsep}{0in}
\setlength{\topsep}{0in}
\setlength{\tabcolsep}{0in}

\definecolor{contactgray}{gray}{0.3}

\definecolor{darkblue}{rgb}{0.0, 0.0, 0.00}
\definecolor{YellowOrange}{rgb}{0.0, 0.0, 0.00}

\pagestyle{empty}

%%%%%%%%%%%%%%%%%%%%%%%%%%
%  Template Definitions  %
%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\lineunder}{\vspace*{-8pt} \\ \hspace*{-6pt} \hrulefill \\ \vspace*{-15pt}}
\newcommand{\name}[1]{\begin{center}\textsc{\color{YellowOrange}\Huge#1}\end{center}}
\newcommand{\program}[1]{\begin{center}\textsc{#1}\end{center}}
\newcommand{\contact}[1]{\begin{center}{\small#1}\end{center}}

\newenvironment{tabbedsection}[1]{
  \begin{list}{}{
      \setlength{\itemsep}{0pt}
      \setlength{\labelsep}{0pt}
      \setlength{\labelwidth}{0pt}
      \setlength{\leftmargin}{3pt}
      \setlength{\rightmargin}{5pt}
      \setlength{\listparindent}{0pt}
      \setlength{\parsep}{0pt}
      \setlength{\parskip}{0pt}
      \setlength{\partopsep}{0pt}
      \setlength{\topsep}{#1}
    }
  \item[]
}{\end{list}}

\newenvironment{nospacetabbing}{\begin{tabbing}}
{\end{tabbing}\vspace{-1.2em}}

\newenvironment{resume_header}{}{\vspace{2pt}}

\newenvironment{resume_section}[1]{
  \filbreak
  \vspace{2\secsep}
  \textsc{\large#1}
  \lineunder
  \begin{tabbedsection}{\secsep}
}{\end{tabbedsection}}

\newenvironment{resume_subsection}[2][]{
  \vspace{\secsep}
  \textbf{#2} \hfill {\small #1} %\hspace{2em}
  \vspace{2 pt}
  \begin{tabbedsection}{0.5\secsep}
}{\end{tabbedsection}}

\newenvironment{education}[3][]{
  \vspace{\secsep}
  \textbf{#2} \hfill {\hspace{-2pt} #3}\\
  \vspace{-13pt}
  \begin{tabbedsection}{\secsep}
}{\end{tabbedsection}}

\newenvironment{subitems}{
  \renewcommand{\labelitemi}{-}
  \begin{itemize}
      \setlength{\labelsep}{0.7em}
}{\end{itemize}}

\newenvironment{nobulletsubitems}{
  \renewcommand{\labelitemi}{} % Remove bullet point
  \begin{itemize}[leftmargin=*]
}{\end{itemize}}

\newenvironment{resume_employer}[4]{
  \vspace{\secsep}
  \textbf{#1} \hfill  {\color{YellowOrange} #3 \vspace{1 pt}}\\ 
  \normalsize{\it #2} \hfill { \small {#4}} \\
  \vspace{-15 pt} 
  \begin{tabbedsection}{0pt}
  \vspace{1.5pt}
  \begin{subitems}
}{\end{subitems}\end{tabbedsection} \vspace{4pt}}

\begin{document}
"""

education = r"""
\begin{resume_section}{Education}
  
  \begin{education}
      {\textcolor{darkblue}{University of Waterloo} - \normalfont Candidate for BASc in Computer Engineering}{\bf 2020 - 2025} 

    \begin{nobulletsubitems}
      \item \textcolor{darkblue}{GPA}: {\bf 3.8}/4.0
      \item \textcolor{darkblue}{Relevant Courses}: Real-time OS (C), Networks (C), Data Structures \& Algorithms (C++), Compilers (Java),\\ Databases (SQL), Hardware (Verilog)
      \item \textcolor{darkblue}{Awards}: President’s Scholarship, Federated Co-op Community Leadership Award, Outstanding Intern
    \end{nobulletsubitems}
    
  \end{education}
  
\end{resume_section}
"""

end = r"\end{document}"
