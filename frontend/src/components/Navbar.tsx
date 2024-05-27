import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import Logo from "../assets/logo.png"
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons"
import { Link } from "react-router-dom"



function Navbar() {
    const navItems = [
        "Contact",
        "Recipes",
        "About"
    ]

    return (
        <>

            <div className="w-11/12 p-2 mx-auto align-center flex justify-between">
                <Link to='/'>
                    <img height={50} width={50} src={Logo} alt="" />
                </Link>
                <div className="">
                    <ul className="flex justify-center align-center p-4 space-x-6 font-semibold text-slate-800">
                        {navItems.map((item) => (
                            <li>
                                <Link to={item.toLowerCase()}>
                                    {item}
                                </Link>
                            </li>
                        ))}
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