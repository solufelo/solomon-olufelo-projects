import Cookies from 'js-cookie'
import { App } from 'antd'
import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
function PublicLayout({ children }: { children: React.ReactNode }) {
  const navigate = useNavigate()
  const { message } = App.useApp()
  
  useEffect(() => {
    const token = Cookies.get('token') || localStorage.getItem('token')
    if (token) {
      navigate('/')
      message.error('You are already logged in')
    }
  }, [navigate, message])
  return (
    <div>
        {children}
    </div>
  )
}

export default PublicLayout