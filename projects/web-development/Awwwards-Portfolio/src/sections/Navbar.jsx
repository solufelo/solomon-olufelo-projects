import React from 'react'
import { useRef } from 'react'
function Navbar() {
  const navRef = useRef(null)
  return (
    <nav
    ref={navRef}
    className="fixed z-50 flex flex-col justify-between w-full
    h-full px-10 uppercase bg-black text-white/80 py-28
    gap-y-10 md:w-1/2 md:left-1/2">
        <div className='flex flex-col text-5xl gap-y-2 md:text-6xl lg:text-8xl'>
            {["home", "about", "contact"].map((item, index) => (
                <Link key={index} href={`#${item}`}>
                    {item}
                </Link>
            ))}
            
        </div>
    </nav>
  )
}

export default Navbar