import { Children, ReactNode } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";



const Layout = ({children}:ILayout) => {
    
    return (
        <div>
            <Navbar />
                {children}
            <Footer />
        </div>
    )
}
export default Layout
