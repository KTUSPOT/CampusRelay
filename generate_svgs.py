import os

svg_dir = os.path.join(os.path.dirname(__file__), "static", "images", "sample")
os.makedirs(svg_dir, exist_ok=True)

images = {
    'casio_calc.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="screenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d1e3d4"/>
      <stop offset="100%" stop-color="#a8c5af"/>
    </linearGradient>
    <linearGradient id="solarGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#451a03"/>
      <stop offset="50%" stop-color="#78350f"/>
      <stop offset="100%" stop-color="#451a03"/>
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="#f8fafc" rx="16"/>
  <!-- Calculator Body -->
  <rect x="80" y="25" width="240" height="350" rx="24" fill="url(#bgGrad)" stroke="#334155" stroke-width="4"/>
  <!-- Top Branding & Solar -->
  <text x="105" y="58" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="14" font-weight="800" letter-spacing="1">CASIO</text>
  <text x="105" y="72" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="8" font-weight="600">fx-991ES PLUS</text>
  <rect x="220" y="44" width="75" height="24" rx="4" fill="url(#solarGrad)" stroke="#92400e" stroke-width="1"/>
  <line x1="245" y1="44" x2="245" y2="68" stroke="#b45309" stroke-width="1"/>
  <line x1="270" y1="44" x2="270" y2="68" stroke="#b45309" stroke-width="1"/>
  <!-- LCD Screen -->
  <rect x="105" y="82" width="190" height="68" rx="8" fill="url(#screenGrad)" stroke="#1e293b" stroke-width="2"/>
  <text x="115" y="104" fill="#1e293b" font-family="monospace" font-size="11" font-weight="bold">∫(0 to π) sin(x) dx</text>
  <text x="285" y="138" fill="#0f172a" font-family="monospace" font-size="18" font-weight="bold" text-anchor="end">= 2</text>
  <text x="115" y="138" fill="#475569" font-family="monospace" font-size="8">[MATH][RAD][D]</text>
  <!-- Function Keys -->
  <rect x="105" y="160" width="28" height="15" rx="4" fill="#ca8a04"/>
  <rect x="145" y="160" width="28" height="15" rx="4" fill="#b91c1c"/>
  <circle cx="200" cy="172" r="18" fill="#64748b" stroke="#334155" stroke-width="2"/>
  <circle cx="200" cy="172" r="8" fill="#1e293b"/>
  <rect x="228" y="160" width="28" height="15" rx="4" fill="#334155"/>
  <rect x="267" y="160" width="28" height="15" rx="4" fill="#334155"/>
  <!-- Scientific Keys Grid -->
  <g fill="#334155">
    <rect x="105" y="186" width="30" height="15" rx="3"/><rect x="145" y="186" width="30" height="15" rx="3"/><rect x="185" y="186" width="30" height="15" rx="3"/><rect x="225" y="186" width="30" height="15" rx="3"/><rect x="265" y="186" width="30" height="15" rx="3"/>
    <rect x="105" y="208" width="30" height="15" rx="3"/><rect x="145" y="208" width="30" height="15" rx="3"/><rect x="185" y="208" width="30" height="15" rx="3"/><rect x="225" y="208" width="30" height="15" rx="3"/><rect x="265" y="208" width="30" height="15" rx="3"/>
    <rect x="105" y="230" width="30" height="15" rx="3"/><rect x="145" y="230" width="30" height="15" rx="3"/><rect x="185" y="230" width="30" height="15" rx="3"/><rect x="225" y="230" width="30" height="15" rx="3"/><rect x="265" y="230" width="30" height="15" rx="3"/>
  </g>
  <!-- Numeric Keypad -->
  <g fill="#cbd5e1">
    <rect x="105" y="254" width="32" height="20" rx="4"/><text x="121" y="269" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">7</text>
    <rect x="145" y="254" width="32" height="20" rx="4"/><text x="161" y="269" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">8</text>
    <rect x="185" y="254" width="32" height="20" rx="4"/><text x="201" y="269" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">9</text>
    <rect x="225" y="254" width="32" height="20" rx="4" fill="#ef4444"/><text x="241" y="269" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">DEL</text>
    <rect x="265" y="254" width="32" height="20" rx="4" fill="#dc2626"/><text x="281" y="269" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">AC</text>

    <rect x="105" y="280" width="32" height="20" rx="4"/><text x="121" y="295" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">4</text>
    <rect x="145" y="280" width="32" height="20" rx="4"/><text x="161" y="295" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">5</text>
    <rect x="185" y="280" width="32" height="20" rx="4"/><text x="201" y="295" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">6</text>
    <rect x="225" y="280" width="32" height="20" rx="4" fill="#64748b"/><text x="241" y="295" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">×</text>
    <rect x="265" y="280" width="32" height="20" rx="4" fill="#64748b"/><text x="281" y="295" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">÷</text>

    <rect x="105" y="306" width="32" height="20" rx="4"/><text x="121" y="321" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">1</text>
    <rect x="145" y="306" width="32" height="20" rx="4"/><text x="161" y="321" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">2</text>
    <rect x="185" y="306" width="32" height="20" rx="4"/><text x="201" y="321" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">3</text>
    <rect x="225" y="306" width="32" height="20" rx="4" fill="#64748b"/><text x="241" y="321" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">+</text>
    <rect x="265" y="306" width="32" height="20" rx="4" fill="#64748b"/><text x="281" y="321" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">-</text>

    <rect x="105" y="332" width="32" height="20" rx="4"/><text x="121" y="347" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">0</text>
    <rect x="145" y="332" width="32" height="20" rx="4"/><text x="161" y="347" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">.</text>
    <rect x="185" y="332" width="32" height="20" rx="4"/><text x="201" y="347" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">×10ˣ</text>
    <rect x="225" y="332" width="32" height="20" rx="4" fill="#64748b"/><text x="241" y="347" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Ans</text>
    <rect x="265" y="332" width="32" height="20" rx="4" fill="#2563eb"/><text x="281" y="347" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">=</text>
  </g>
</svg>''',

    'mini_drafter.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="steelGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e2e8f0"/>
      <stop offset="50%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
    <linearGradient id="brassGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fde047"/>
      <stop offset="50%" stop-color="#ca8a04"/>
      <stop offset="100%" stop-color="#854d0e"/>
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="#f1f5f9" rx="16"/>
  <rect x="35" y="35" width="330" height="330" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" rx="6"/>
  <rect x="45" y="45" width="310" height="310" fill="none" stroke="#93c5fd" stroke-width="1" stroke-dasharray="6 4"/>
  <rect x="40" y="35" width="40" height="50" fill="#1e293b" rx="4"/>
  <circle cx="60" cy="60" r="14" fill="url(#brassGrad)" stroke="#78350f" stroke-width="2"/>
  <line x1="60" y1="60" x2="180" y2="140" stroke="url(#steelGrad)" stroke-width="8" stroke-linecap="round"/>
  <line x1="65" y1="55" x2="185" y2="135" stroke="url(#steelGrad)" stroke-width="4" stroke-linecap="round"/>
  <circle cx="180" cy="140" r="16" fill="#334155" stroke="#0f172a" stroke-width="3"/>
  <circle cx="180" cy="140" r="6" fill="url(#brassGrad)"/>
  <line x1="180" y1="140" x2="260" y2="245" stroke="url(#steelGrad)" stroke-width="8" stroke-linecap="round"/>
  <line x1="185" y1="135" x2="265" y2="240" stroke="url(#steelGrad)" stroke-width="4" stroke-linecap="round"/>
  <g transform="translate(260, 245)">
    <circle cx="0" cy="0" r="32" fill="#ffffff" stroke="#0284c7" stroke-width="3" opacity="0.95"/>
    <circle cx="0" cy="0" r="12" fill="url(#brassGrad)" stroke="#78350f" stroke-width="2"/>
    <path d="M-28 0 A28 28 0 0 1 28 0" fill="none" stroke="#0369a1" stroke-width="2" stroke-dasharray="3 3"/>
    <rect x="0" y="-8" width="95" height="16" fill="rgba(56, 189, 248, 0.45)" stroke="#0284c7" stroke-width="1.5" rx="2"/>
    <line x1="20" y1="-8" x2="20" y2="-2" stroke="#0f172a" stroke-width="1"/>
    <line x1="40" y1="-8" x2="40" y2="-1" stroke="#0f172a" stroke-width="1"/>
    <line x1="60" y1="-8" x2="60" y2="-2" stroke="#0f172a" stroke-width="1"/>
    <line x1="80" y1="-8" x2="80" y2="-1" stroke="#0f172a" stroke-width="1"/>
    <rect x="-8" y="0" width="16" height="95" fill="rgba(56, 189, 248, 0.45)" stroke="#0284c7" stroke-width="1.5" rx="2"/>
    <line x1="-8" y1="20" x2="-2" y2="20" stroke="#0f172a" stroke-width="1"/>
    <line x1="-8" y1="40" x2="-1" y2="40" stroke="#0f172a" stroke-width="1"/>
    <line x1="-8" y1="60" x2="-2" y2="60" stroke="#0f172a" stroke-width="1"/>
    <line x1="-8" y1="80" x2="-1" y2="80" stroke="#0f172a" stroke-width="1"/>
  </g>
  <text x="200" y="375" fill="#0369a1" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">OMEGA DELUXE MINI DRAFTER</text>
</svg>''',

    'drawing_board.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="woodGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="25%" stop-color="#b45309"/>
      <stop offset="50%" stop-color="#d97706"/>
      <stop offset="75%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="ebonyGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="#f8fafc" rx="16"/>
  <g transform="translate(30, 60)">
    <rect x="0" y="0" width="340" height="250" rx="6" fill="url(#woodGrad)" stroke="#92400e" stroke-width="3"/>
    <line x1="0" y1="50" x2="340" y2="50" stroke="#92400e" stroke-width="1.5" opacity="0.4"/>
    <line x1="0" y1="100" x2="340" y2="100" stroke="#78350f" stroke-width="1.5" opacity="0.4"/>
    <line x1="0" y1="150" x2="340" y2="150" stroke="#92400e" stroke-width="1.5" opacity="0.4"/>
    <line x1="0" y1="200" x2="340" y2="200" stroke="#78350f" stroke-width="1.5" opacity="0.4"/>
    <rect x="0" y="0" width="18" height="250" fill="url(#ebonyGrad)" rx="4"/>
    <rect x="45" y="25" width="265" height="200" fill="#ffffff" stroke="#e2e8f0" stroke-width="2" rx="3"/>
    <circle cx="55" cy="35" r="5" fill="#ef4444" stroke="#991b1b" stroke-width="1"/>
    <circle cx="300" cy="35" r="5" fill="#ef4444" stroke="#991b1b" stroke-width="1"/>
    <circle cx="55" cy="215" r="5" fill="#ef4444" stroke="#991b1b" stroke-width="1"/>
    <circle cx="300" cy="215" r="5" fill="#ef4444" stroke="#991b1b" stroke-width="1"/>
    <rect x="190" y="180" width="110" height="35" fill="none" stroke="#0284c7" stroke-width="1.5"/>
    <text x="245" y="196" fill="#0369a1" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">ENGINEERING GRAPHICS</text>
    <text x="245" y="208" fill="#64748b" font-family="monospace" font-size="7" text-anchor="middle">SHEET NO: 01 | D2 IMPERIAL</text>
  </g>
  <text x="200" y="355" fill="#b45309" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">IMPERIAL D2 WOODEN BOARD (800x600mm)</text>
</svg>''',

    'drawing_kit.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="velvetGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#312e81"/>
    </linearGradient>
    <linearGradient id="brassShine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#eab308"/>
      <stop offset="100%" stop-color="#a16207"/>
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="#f8fafc" rx="16"/>
  <rect x="35" y="40" width="330" height="300" rx="14" fill="url(#velvetGrad)" stroke="#4338ca" stroke-width="4"/>
  <g transform="translate(120, 70)">
    <circle cx="25" cy="15" r="9" fill="url(#brassShine)" stroke="#713f12" stroke-width="1.5"/>
    <line x1="20" y1="20" x2="5" y2="140" stroke="#e2e8f0" stroke-width="6" stroke-linecap="round"/>
    <line x1="30" y1="20" x2="45" y2="140" stroke="#e2e8f0" stroke-width="6" stroke-linecap="round"/>
    <rect x="10" y="65" width="30" height="8" rx="2" fill="url(#brassShine)"/>
    <line x1="2" y1="69" x2="48" y2="69" stroke="#cbd5e1" stroke-width="2"/>
    <line x1="5" y1="140" x2="3" y2="165" stroke="#64748b" stroke-width="2"/>
    <rect x="42" y="135" width="6" height="20" fill="#334155"/>
    <line x1="45" y1="155" x2="45" y2="165" stroke="#0f172a" stroke-width="3"/>
  </g>
  <g transform="translate(210, 70)">
    <circle cx="25" cy="15" r="8" fill="url(#brassShine)" stroke="#713f12" stroke-width="1.5"/>
    <line x1="22" y1="20" x2="10" y2="140" stroke="#cbd5e1" stroke-width="5" stroke-linecap="round"/>
    <line x1="28" y1="20" x2="40" y2="140" stroke="#cbd5e1" stroke-width="5" stroke-linecap="round"/>
    <line x1="10" y1="140" x2="8" y2="165" stroke="#64748b" stroke-width="2"/>
    <line x1="40" y1="140" x2="42" y2="165" stroke="#64748b" stroke-width="2"/>
  </g>
  <polygon points="60,240 140,240 60,160" fill="rgba(147, 197, 253, 0.5)" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="75,230 120,230 75,185" fill="#1e1b4b"/>
  <path d="M270,160 C320,180 330,220 290,250 C260,270 290,300 320,280 C335,270 310,230 295,200 Z" fill="rgba(253, 224, 71, 0.4)" stroke="#eab308" stroke-width="2"/>
  <rect x="170" y="260" width="50" height="20" rx="3" fill="#059669" stroke="#10b981" stroke-width="1.5"/>
  <text x="195" y="274" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">0.5 2H</text>
  <text x="200" y="370" fill="#4338ca" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">ENGINEERING INSTRUMENT SET</text>
</svg>''',

    'math_book.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="navyBook" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="goldAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="#f8fafc" rx="16"/>
  <g transform="translate(85, 40)">
    <rect x="-15" y="10" width="25" height="310" rx="4" fill="#172554" stroke="#0f172a" stroke-width="2"/>
    <rect x="225" y="15" width="15" height="300" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="230" height="320" rx="8" fill="url(#navyBook)" stroke="#1e40af" stroke-width="3"/>
    <rect x="0" y="25" width="230" height="8" fill="url(#goldAccent)"/>
    <text x="115" y="70" fill="#ffffff" font-family="serif, system-ui" font-size="18" font-weight="bold" text-anchor="middle" letter-spacing="1">HIGHER</text>
    <text x="115" y="95" fill="#60a5fa" font-family="serif, system-ui" font-size="18" font-weight="bold" text-anchor="middle">ENGINEERING</text>
    <text x="115" y="120" fill="#fbbf24" font-family="serif, system-ui" font-size="18" font-weight="bold" text-anchor="middle">MATHEMATICS</text>
    <rect x="45" y="135" width="140" height="2" fill="url(#goldAccent)"/>
    <rect x="30" y="150" width="170" height="85" rx="6" fill="rgba(255, 255, 255, 0.07)" stroke="#3b82f6" stroke-width="1"/>
    <text x="115" y="175" fill="#93c5fd" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">∇²ψ = (1/c²) ∂²ψ/∂t²</text>
    <text x="115" y="198" fill="#cbd5e1" font-family="monospace" font-size="10" text-anchor="middle">L{f(t)} = ∫₀^∞ e⁻ˢᵗ f(t) dt</text>
    <text x="115" y="220" fill="#fbbf24" font-family="monospace" font-size="10" text-anchor="middle">det(A - λI) = 0</text>
    <text x="115" y="265" fill="#ffffff" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">B. S. GREWAL</text>
    <rect x="65" y="280" width="100" height="20" rx="10" fill="#dc2626"/>
    <text x="115" y="294" fill="#ffffff" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="middle">44th EDITION</text>
  </g>
</svg>''',

    'graphics_book.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="crimsonBook" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#881337"/>
      <stop offset="100%" stop-color="#4c0519"/>
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="#f8fafc" rx="16"/>
  <g transform="translate(85, 40)">
    <rect x="-15" y="10" width="25" height="310" rx="4" fill="#4c0519" stroke="#2e020d" stroke-width="2"/>
    <rect x="225" y="15" width="15" height="300" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="230" height="320" rx="8" fill="url(#crimsonBook)" stroke="#be123c" stroke-width="3"/>
    <rect x="0" y="25" width="230" height="6" fill="#f43f5e"/>
    <text x="115" y="65" fill="#fecdd3" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle" letter-spacing="2">ELEMENTARY</text>
    <text x="115" y="90" fill="#ffffff" font-family="system-ui, sans-serif" font-size="18" font-weight="800" text-anchor="middle">ENGINEERING</text>
    <text x="115" y="115" fill="#f43f5e" font-family="system-ui, sans-serif" font-size="18" font-weight="800" text-anchor="middle">DRAWING</text>
    <g transform="translate(115, 195)">
      <polygon points="0,-30 35,-10 0,10 -35,-10" fill="#fb7185" stroke="#ffffff" stroke-width="1.5"/>
      <polygon points="-35,-10 0,10 0,45 -35,25" fill="#e11d48" stroke="#ffffff" stroke-width="1.5"/>
      <polygon points="0,10 35,-10 35,25 0,45" fill="#9f1239" stroke="#ffffff" stroke-width="1.5"/>
    </g>
    <text x="115" y="270" fill="#ffffff" font-family="system-ui, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">N. D. BHATT</text>
    <text x="115" y="290" fill="#fda4af" font-family="system-ui, sans-serif" font-size="9" text-anchor="middle">Charotar Publishing House</text>
  </g>
</svg>''',

    'electronics_book.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="emeraldBook" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#065f46"/>
      <stop offset="100%" stop-color="#022c22"/>
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="#f8fafc" rx="16"/>
  <g transform="translate(85, 40)">
    <rect x="-15" y="10" width="25" height="310" rx="4" fill="#022c22" stroke="#011a14" stroke-width="2"/>
    <rect x="225" y="15" width="15" height="300" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="230" height="320" rx="8" fill="url(#emeraldBook)" stroke="#059669" stroke-width="3"/>
    <rect x="0" y="25" width="230" height="6" fill="#34d399"/>
    <text x="115" y="70" fill="#a7f3d0" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">BASIC</text>
    <text x="115" y="95" fill="#ffffff" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">ELECTRICAL &amp;</text>
    <text x="115" y="120" fill="#34d399" font-family="system-ui, sans-serif" font-size="17" font-weight="800" text-anchor="middle">ELECTRONICS</text>
    <g transform="translate(65, 145)">
      <rect x="0" y="0" width="100" height="75" fill="rgba(0,0,0,0.25)" stroke="#10b981" stroke-width="1.5" rx="4"/>
      <line x1="10" y1="38" x2="25" y2="38" stroke="#34d399" stroke-width="2"/>
      <polyline points="25,38 30,30 35,46 40,30 45,46 50,38" fill="none" stroke="#34d399" stroke-width="2"/>
      <line x1="50" y1="38" x2="65" y2="38" stroke="#34d399" stroke-width="2"/>
      <line x1="65" y1="26" x2="65" y2="50" stroke="#34d399" stroke-width="2"/>
      <line x1="72" y1="26" x2="72" y2="50" stroke="#34d399" stroke-width="2"/>
      <line x1="72" y1="38" x2="90" y2="38" stroke="#34d399" stroke-width="2"/>
      <text x="50" y="65" fill="#6ee7b7" font-family="monospace" font-size="8" text-anchor="middle">R-L-C TRANSIENT</text>
    </g>
    <text x="115" y="260" fill="#ffffff" font-family="system-ui, sans-serif" font-size="13" font-weight="bold" text-anchor="middle">B. L. THERAJA</text>
    <text x="115" y="280" fill="#6ee7b7" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">S. Chand &amp; Company</text>
  </g>
</svg>''',

    'mechanics_book.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="slateBook" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="#f8fafc" rx="16"/>
  <g transform="translate(85, 40)">
    <rect x="-15" y="10" width="25" height="310" rx="4" fill="#0f172a" stroke="#020617" stroke-width="2"/>
    <rect x="225" y="15" width="15" height="300" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="230" height="320" rx="8" fill="url(#slateBook)" stroke="#64748b" stroke-width="3"/>
    <rect x="0" y="25" width="230" height="6" fill="#f59e0b"/>
    <text x="115" y="70" fill="#fcd34d" font-family="system-ui, sans-serif" font-size="14" font-weight="bold" text-anchor="middle">ENGINEERING</text>
    <text x="115" y="98" fill="#ffffff" font-family="system-ui, sans-serif" font-size="20" font-weight="800" text-anchor="middle">MECHANICS</text>
    <g transform="translate(55, 145)">
      <polygon points="10,60 60,10 110,60" fill="rgba(251, 191, 36, 0.1)" stroke="#fbbf24" stroke-width="2"/>
      <line x1="60" y1="10" x2="60" y2="60" stroke="#fbbf24" stroke-width="2"/>
      <line x1="60" y1="0" x2="60" y2="10" stroke="#ef4444" stroke-width="3"/>
      <polygon points="60,10 56,2 64,2" fill="#ef4444"/>
      <text x="60" y="72" fill="#fcd34d" font-family="monospace" font-size="8" text-anchor="middle">Σ Fx=0, Σ Fy=0, Σ M=0</text>
    </g>
    <text x="115" y="260" fill="#ffffff" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">S. TIMOSHENKO &amp; D. H. YOUNG</text>
    <text x="115" y="280" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">McGraw Hill Education</text>
  </g>
</svg>'''
}

for name, content in images.items():
    filepath = os.path.join(svg_dir, name)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"Generated {name}")
