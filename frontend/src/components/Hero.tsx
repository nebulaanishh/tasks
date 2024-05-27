import { Link } from 'react-router-dom'
import heroImage from '../assets/plate.png'
// import heroImage from '../assets/food.json'

function Hero() {

    return (
        <>
            <section>
                <div className="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8 lg:py-16">
                    <div className="grid grid-cols-1 gap-8 lg:grid-cols-2 lg:gap-16">
                        <div className="relative h-64 overflow-hidden rounded-lg sm:h-80 lg:order-last lg:h-full">
                            <img
                                alt=""
                                src={heroImage}
                                className="absolute inset-0 h-full w-full object-cover"
                            />
                        </div>

                        <div className="lg:py-24">
                            <h2 className="text-3xl font-bold sm:text-4xl">Easy Food Recipes</h2>

                            <p className="mt-4 text-gray-600">
                            Discover delicious recipes on our food website! From quick meals to gourmet dishes, we offer easy-to-follow instructions, stunning photos, and tips for all skill levels. Start cooking today!
                            </p>

                            <a
                                href="#"
                                
                            >
                                <Link to='recipes' className="mt-8 inline-block rounded bg-indigo-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-indigo-700 focus:outline-none focus:ring focus:ring-yellow-400">

                                View all recipes
                                </Link>
                            </a>
                        </div>
                    </div>
                </div>
            </section>
        </>
    )
}

export default Hero