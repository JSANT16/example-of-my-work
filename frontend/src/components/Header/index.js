import { H1, HeaderElement, MenuContainer, MenuLinkContainer, MenuLink } from "./HederElements"
export default function Header() {
    return (
        <HeaderElement>
            <H1 ><MenuLink to="/">Mobilender</MenuLink></H1>
            <MenuContainer>
                <MenuLinkContainer><MenuLink to="/articles" >Articles</MenuLink></MenuLinkContainer>
                <MenuLinkContainer><MenuLink to="/vendors">Vendors</MenuLink></MenuLinkContainer>
                <MenuLinkContainer><MenuLink to="/orders">Orders</MenuLink></MenuLinkContainer>
                <MenuLinkContainer><MenuLink to="/">Dashboard</MenuLink></MenuLinkContainer>
                <MenuLinkContainer><MenuLink to="/custumers">Custumers</MenuLink></MenuLinkContainer>

            </MenuContainer>
        </HeaderElement>
    )
}