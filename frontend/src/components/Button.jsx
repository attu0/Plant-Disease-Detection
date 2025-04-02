import './Button.css'

function Button({ text, onClick, type = "primary", disabled = false }) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={`custom-button ${type}`}
    >
      {text}
    </button>
  )
}

export default Button 