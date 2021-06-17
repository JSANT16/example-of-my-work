import styled from 'styled-components'
import { Link } from 'react-router-dom'
export const HeaderElement = styled.header`
background-color: #00427a;
max-width: 100%;
padding: 2em;
`

export const H1 = styled.h1`
color: #fff;
`
export const MenuContainer = styled.ul`
 list-style-type: none;
  margin: 0;
  padding: 0;
`
export const MenuLinkContainer = styled.li`
display:inline-block;
    width:10%;
    padding:5px 10px;
    text-align:center;
    color:#fff;
`
export const MenuLink = styled(Link)`
text-decoration:none;
color:#fff;
 &:hover {
        color: #7cb73b;;
        transition: all 0.3s ease;
    }
`