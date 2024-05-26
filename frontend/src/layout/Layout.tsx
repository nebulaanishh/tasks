import { Children, ReactNode } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";



const Layout = ({children}:any) => {
    
    return (
        <div className="bg-yellow-500">
            <Navbar />
                {children}
            <Footer />
        </div>
    )
}
export default Layout
