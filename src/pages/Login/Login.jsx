import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../../services/api";
import "./Login.css";

function Login() {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const [message, setMessage] = useState("");

    const [loading, setLoading] = useState(false);

    const handleLogin = async (e) => {

        e.preventDefault();

        if (!email || !password) {

            setMessage("Please fill all fields.");

            return;
        }

        try {

            setLoading(true);

            const response = await api.post("/login", {

                email,

                password

            });

            localStorage.setItem("token", response.data.token);

            localStorage.setItem("name", response.data.name);

            navigate("/home");

        }

        catch (error) {

            if (error.response) {

                setMessage(error.response.data.message);

            }

            else {

                setMessage("Server Error");

            }

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <div className="login-container">

            <div className="login-left">

                <h1>Welcome Back</h1>

                <p>

                    Login to continue using AI Healthcare Assistant.

                </p>

                <form onSubmit={handleLogin}>

                    <input

                        type="email"

                        placeholder="Email Address"

                        value={email}

                        onChange={(e)=>setEmail(e.target.value)}

                    />

                    <input

                        type="password"

                        placeholder="Password"

                        value={password}

                        onChange={(e)=>setPassword(e.target.value)}

                    />

                    <button type="submit">

                        {

                            loading ?

                            "Logging in..."

                            :

                            "Login"

                        }

                    </button>

                </form>

                {

                    message &&

                    <p className="error">

                        {message}

                    </p>

                }

                <p className="register-link">

                    Don't have an account?

                    <Link to="/register">

                        Register

                    </Link>

                </p>

            </div>

            <div className="login-right">

                <img

                    src="https://images.unsplash.com/photo-1584515933487-779824d29309?w=900"

                    alt="Healthcare"

                />

            </div>

        </div>

    );

}

export default Login;