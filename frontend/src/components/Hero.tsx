import heroImage from '../assets/hero.jpg'

function Hero() {

    return (
        <>
            <div className="h-screen bg-slate-400">

                <div className="relative">
                <div className='absolute inset-0 bg-black opacity-40'></div>
                {/* <img src={heroImage} alt="Image" className="" /> */}

                <img className='bg-blend-darken' height={500} width={2000} src={heroImage} alt="" />
                </div>
            </div>
        </>
    )
}

export default Hero