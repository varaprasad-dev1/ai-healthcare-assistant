import "./Navbar.css";
import { Link, useNavigate } from "react-router-dom";
import { FaUserCircle } from "react-icons/fa";

function Navbar() {

    const navigate = useNavigate();

    const user = localStorage.getItem("name");

    const logout = () => {

        localStorage.removeItem("token");

        localStorage.removeItem("name");

        navigate("/login");

    };

    return (

        <nav className="navbar">

            <div className="logo">

                🏥 AI Healthcare

            </div>

            <ul className="nav-links">

                <li>

                    <Link to="/home">

                        Home

                    </Link>

                </li>

                <li>

                    <Link to="/chatbot">

                        AI Chat

                    </Link>

                </li>

                <li>

                    <Link to="/medicine">

                        Medicines

                    </Link>

                </li>

                <li>

                    <Link to="/dashboard">

                        Dashboard

                    </Link>

                </li>

                <li>

                    <Link to="/profile">

                        Profile

                    </Link>

                </li>

            </ul>

            <div className="user-section">

                <FaUserCircle
                    size={30}
                />

                <span>

                    {user}

                </span>

                <button

                    onClick={logout}

                >

                    Logout

                </button>

            </div>

        </nav>

    );

}

export default Navbar;