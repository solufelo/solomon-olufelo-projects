import logo from "../../../assets/logo-helmet-TRANSPARENT_.png"
export default function WelcomeContent() {
  return (
    <div className="text-white text">
      <div className="flex flex-col items-center justify-center ">
        <img src={logo} alt="logo" className="w-110 h-90 object-contain " />
        <h1 className="text-6xl font-bold text-center text-[#A6D1FF] " >CAPTAIN - FUNDS</h1>
        <p className="text-center text-md text-gray-200">Happiness doesnt result from what we get, but from what we give.</p>
      </div>
      </div>
  )
}
