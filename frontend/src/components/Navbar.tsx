import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import Logo from  "../assets/logo.png" 
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons"



function Navbar(){
    const navItems = [
        "Contact",
        "Recipes",
        "About"
    ]

    return (
        <>
            <div className="w-11/12 p-2 bg-yellow-500 mx-auto align-center flex justify-between">
                <img height={50} width={50} src={Logo} alt="" />
                <div className="">
                    <ul className="flex justify-center align-center p-4 space-x-6 font-semibold text-slate-800">
                    {navItems.map( (item) => (
                        <li> {item} </li>
                    ) )}
                    <form action="" className="">
                    <FontAwesomeIcon icon={faMagnifyingGlass} />
                        <input className="px-4" placeholder="Search" type="Enter to search" />
                    </form>
                    </ul>

                    
                </div>

            </div>
        </>
    )
}

export default Navbar