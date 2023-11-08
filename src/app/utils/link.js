import {default as NextLink} from 'next/link'


export default function Link ({className, children, ...props}) {
    const linkCSS = "text-blue-500 hover:text-blue-900"
    return <NextLink className={linkCSS} {...props}>{children}</NextLink>
}